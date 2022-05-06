from http import HTTPStatus
from flask import request, jsonify
from app.config.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from app.controllers.address_controller import register_address
from app.models.partners import PartnerModel
from app.config.auth import auth

@auth.login_required(role="admin")
def register_partner():
    #adm route
    session: Session = db.session()

    data = request.get_json()

    address = register_address(data["address"])

    data.pop("address")
    data["id_address"] = address.id

    partner_info = PartnerModel(**data)

    session.add(partner_info)
    session.commit()

    return jsonify(partner_info), HTTPStatus.CREATED

@auth.login_required
def get_partners():
    base_query: Query = db.session.query(PartnerModel)
    
    records = base_query.all()

    return jsonify(records), HTTPStatus.OK

@auth.login_required
def get_partner_by_id(partner_id):
    partner: PartnerModel = PartnerModel.query.filter_by(id=partner_id).first()

    if partner:
        return jsonify(partner), HTTPStatus.OK
    return {"msg": "Parceiro não encontrado"}, HTTPStatus.NOT_FOUND
    