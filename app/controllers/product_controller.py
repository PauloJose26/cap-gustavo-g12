
from flask import request, current_app, jsonify
from app.models.products import ProductModel
from datetime import datetime, timedelta
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

def register_product():
    now = datetime.now()
    data = request.get_json()
    cpf = data.get('cpf')
    data["first_shot_date"] = now
    data["second_shot_date"] = (now + timedelta(days=90))
    
    if len(cpf) != 11:
        return {"error": "Invalid CPF"}, HTTPStatus.BAD_REQUEST
    
    if any(type(field) != str for field in data):
        return {"error": "All fields must be submitted as strings"}, HTTPStatus.BAD_REQUEST
    
    if ["cpf", "name", "vaccine_name","health_unit_name"] == data.keys():
        return {"error": "Please, fill out every field required. "}, HTTPStatus.BAD_REQUEST

  
    new_vaccine = VaccineModel(**data)
    try:
        current_app.db.session.add(new_vaccine)
        current_app.db.session.commit()

        return jsonify(new_vaccine), HTTPStatus.CREATED
    except IntegrityError:
        return {"error": "CPF already registered"}, HTTPStatus.CONFLICT
    ...

def update_product(product_id):
    # partner_id = request.args.get("partner_id")
    ...

def get_products():
    # partner_id = request.args.get("partner_id")
    ...

def get_product_by_id(product_id):
    # partner_id = request.args.get("partner_id")
    ...