from http import HTTPStatus
from flask import request, jsonify
from app.config.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from app.controllers.address_controller import register_address
from app.models.users import UserModel

def register_user():
    session: Session = db.session()

    data = request.get_json()

    address = register_address(data["address"])

    data.pop("address")
    data["id_address"] = address.id

    user_info = UserModel(**data)

    session.add(user_info)
    session.commit()

    return jsonify(user_info), HTTPStatus.CREATED

def update_user(user_id):
    ...

def delete_user(user_id):
    session: Session = db.session()

    record = session.query(UserModel).get(user_id)

    session.delete(record)

    session.commit()

    return "", HTTPStatus.NO_CONTENT

def get_user():
    # adm route
    base_query: Query = db.session.query(UserModel)
    
    records = base_query.all()

    return jsonify(records), HTTPStatus.OK

def get_user_by_id(user_id):
    # adm route
    ...