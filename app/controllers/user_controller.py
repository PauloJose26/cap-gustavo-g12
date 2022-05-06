from http import HTTPStatus
from flask import current_app, request, jsonify
from psycopg2 import IntegrityError
from app.config.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from app.controllers.address_controller import register_address
from app.models.users import UserModel
from app.models.addresses import AddressModel
import secrets
from app.config.auth import auth
from sqlalchemy.exc import DataError, IntegrityError


def register_user():
    try: 
        session: Session = db.session()

        data = request.get_json()

        password_to_hash = data.pop("password")

        address = register_address(data["address"])

        data.pop("address")
        data["id_address"] = address.id

        data["api_key"] = secrets.token_urlsafe(32)

        data["role"] = "user"

        user_info = UserModel(**data)

        user_info.password = password_to_hash

        session.add(user_info)
        session.commit()

        return jsonify(user_info), HTTPStatus.CREATED
    except (TypeError, IntegrityError) as err:
        if "(psycopg2.errors.UniqueViolation)" in str(err):
            return {"error msg": "cpf or email already exists"}, HTTPStatus.CONFLICT
        return {"error msg" : "key missing or wrong spelling", "keys user": ["name", "email", "cpf", "phone_number", "birth_date", "password"], "keys address": ["country", "state", "city", "street", "number", "complement", "postal_code"]}, HTTPStatus.BAD_REQUEST

@auth.login_required
def update_user(user_id):
    data = request.get_json()
    session = current_app.db.session
    user: UserModel = UserModel.query.filter_by(id=user_id).first()
    try:
        for key, value in data.items():
            setattr(user, key, value)

        session.add(user)
        session.commit()

        return data, HTTPStatus.OK

    except IntegrityError as err:
        if "(psycopg2.errors.UniqueViolation)" in str(err):
            return (
                jsonify(error=f"email already exists"),
                HTTPStatus.CONFLICT,
            )
    except:
        return {"msg": "Usuário não encontrado"}, HTTPStatus.NOT_FOUND


@auth.login_required
def delete_user(user_id):
    try:
        session: Session = db.session()

        user_record = session.query(UserModel).get(user_id)

        address_record = session.query(AddressModel).get(user_record.id_address)

        if user_record.role == "admin":
            return {"error": "Cannot Delete an Admin"}, HTTPStatus.UNAUTHORIZED

        session.delete(user_record)
        session.commit()
        session.delete(address_record)
        session.commit()

        return "", HTTPStatus.NO_CONTENT
    except DataError:
        return {"error": "Usuário não encontrado"}, HTTPStatus.NOT_FOUND


@auth.login_required(role="admin")
def get_user():
    base_query: Query = db.session.query(UserModel)

    records = base_query.all()

    return jsonify(records), HTTPStatus.OK

@auth.login_required(role="admin")
def get_user_by_id(user_id):
    user: UserModel = UserModel.query.filter_by(id=user_id).first()
    if user:
        return jsonify(user), HTTPStatus.OK
    return {"msg": "Usuário não encontrado"}, HTTPStatus.NOT_FOUND


def login():
    session: Session = db.session()

    data = request.get_json()

    user = session.query(UserModel).filter_by(email=data["email"]).first()

    if not user:
        return {"error": "Usuário não encontrado"}, HTTPStatus.NOT_FOUND

    if user.verify_password(data["password"]):
        return {"Access Token": user.api_key}, HTTPStatus.OK
    else:
        return {"error": "Não autorizado"}, HTTPStatus.UNAUTHORIZED
