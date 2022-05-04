from itertools import product
from flask import request, current_app, jsonify
from app.config.database import db
from app.models.products import ProductModel
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from datetime import datetime, timedelta
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError



def register_product():
    from app.tasks.close_auction_task import close_auction
    
    session: Session = db.session()

    data = request.get_json()

    partner_id = 1

    data["partner_id"] = partner_id
    
    product_info = ProductModel(**data)
    
    session.add(product_info)
    session.commit()
    
    task = close_auction.delay(product_info["id"], data["auction_end"])
    data["task_id"] = task.id
    
    product_info = ProductModel(**data)
    
    session.add(product_info)
    session.commit()

    return jsonify(product_info), HTTPStatus.CREATED



def update_product(product_id):
    session: Session = db.session()

    data = request.get_json()

    product: Query = db.session.query(ProductModel).filter_by(id = product_id).first()

    for key, value in data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()

    return jsonify(product), HTTPStatus.ACCEPTED



def get_products():
    products_list_query: Query = db.session.query(ProductModel)
    products_list = products_list_query.all()

    return jsonify(products_list), HTTPStatus.OK



def get_product_by_id(product_id):
    product: Query = db.session.query(ProductModel).filter_by(id = product_id).first()

    return jsonify(product), HTTPStatus.OK
