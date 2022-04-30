
from flask import request, current_app, jsonify
from app.models.products import ProductModel
from datetime import datetime, timedelta
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

def register_product():
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