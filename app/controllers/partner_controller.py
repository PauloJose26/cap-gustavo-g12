from http import HTTPStatus
from flask import request, jsonify
from app.config.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from app.controllers.address_controller import register_address
from app.models.partners import PartnerModel

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

def get_partners():
    base_query: Query = db.session.query(PartnerModel)
    
    records = base_query.all()

    return jsonify(records), HTTPStatus.OK

def get_partner_by_id(partner_id):
    ...
    