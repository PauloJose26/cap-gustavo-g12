from itertools import product
from flask import request,  jsonify
from app.config.database import db
from app.models.categories import CategorieModel
from app.models.products import ProductModel
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from datetime import datetime, timedelta
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.config.auth import auth


@auth.login_required(role="admin")
def register_product():
    from app.tasks import close_auction, open_auction

    session: Session = db.session()

    data:dict = request.get_json()

    partner_id = "e5a4ab88-73ce-444b-b672-2f1bfa549e7c" #MOCK. Fazer autenticação.

    data["partner_id"] = partner_id
    
    try:
        
        if data.get("categories"):
            for i in data["categories"]:
                product_category = session.query(CategorieModel).filter_by(name = i).first()
                if product_category:
                    product_info.categories.append(product_category)
        
        product_info = ProductModel(**data)
        
        session.add(product_info)
        session.commit()

        open_time = datetime.strptime(data["auction_start"], "%Y-%m-%d %H:%M") - datetime.now()
        open_auction.delay(product_info.id, open_time.seconds)
        
        close_time = datetime.strptime(data["auction_end"], "%Y-%m-%d %H:%M") - datetime.now()
        task = close_auction.delay(product_info.id, close_time.seconds)
        
        
        setattr(product_info, "task_id", task.task_id)
        
        session.add(product_info)
        session.commit()


        return jsonify(product_info), HTTPStatus.CREATED
    except:
        #tratar possíveis erros no registro do produto
        {"erro":"Verifique sua requisição"}, HTTPStatus.BAD_REQUEST


@auth.login_required(role="admin")
def update_product(product_id):
    session: Session = db.session()

    data = request.get_json()

    product: Query = db.session.query(ProductModel).filter_by(id = product_id).first()

    for key, value in data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()

    return jsonify(product), HTTPStatus.ACCEPTED


@auth.login_required
def get_products():
    products_list_query: Query = db.session.query(ProductModel)
    products_list = products_list_query.all()

    return jsonify(products_list), HTTPStatus.OK


@auth.login_required
def get_product_by_id(product_id):
    product: Query = db.session.query(ProductModel).filter_by(id = product_id).first()

    return jsonify(product), HTTPStatus.OK
