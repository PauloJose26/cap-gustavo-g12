from http import HTTPStatus
from flask import current_app, request, jsonify
from psycopg2 import IntegrityError
from app.config.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from app.controllers.address_controller import register_address
from app.models.users import UserModel
import secrets
from app.config.auth import auth


def register_user():
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
    session: Session = db.session()

    record = session.query(UserModel).get(user_id)
    print(record)

    if record.role == "admin":
        return {"error": "Cannot Delete an Admin"}, HTTPStatus.UNAUTHORIZED

    session.delete(record)

    session.commit()

    return "", HTTPStatus.NO_CONTENT


@auth.login_required(role="admin")
def get_user():
    # adm route
    base_query: Query = db.session.query(UserModel)

    records = base_query.all()

    return jsonify(records), HTTPStatus.OK


def get_user_by_id(user_id):
    # adm route
    user: UserModel = UserModel.query.filter_by(id=user_id).first()
    if user:
        return jsonify(user), HTTPStatus.OK
    return {"msg": "Usuário não encontrado"}, HTTPStatus.NOT_FOUND


def login():
    session: Session = db.session()

    data = request.get_json()

    user = session.query(UserModel).filter_by(email=data["email"]).first()

    if not user:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    if user.verify_password(data["password"]):
        return {"Access Token": user.api_key}, HTTPStatus.OK
    else:
        return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
