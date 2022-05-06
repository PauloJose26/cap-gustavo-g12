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
from dotenv import load_dotenv
import os
from app.config.auth import auth_user, auth_partner

load_dotenv()



@auth_partner.login_required
def register_product():
    from app.tasks import close_auction, open_auction

    session: Session = db.session()

    data:dict = request.get_json()

    data["partner_id"] = auth_user.current_user().id
    open_time = datetime.strptime(data["auction_start"], "%Y-%m-%d %H:%M") - datetime.now()
    close_time = datetime.strptime(data["auction_end"], "%Y-%m-%d %H:%M") - datetime.now()
    
    try:
        new_list = []
        if data.get("categories"):
            new_list = data["categories"]
            data.pop("categories")
        product_info = ProductModel(**data)

        if new_list:
            for i in new_list:
                product_category = session.query(CategorieModel).filter_by(name = i).first()
                if product_category:
                    product_info.categories.append(product_category)

        session.add(product_info)
        session.commit()

        open_auction.delay(product_info.id, open_time.seconds)
        task = close_auction.delay(product_info.id, close_time.seconds)


        setattr(product_info, "task_id", task.task_id)

        # session.add(product_info)
        session.commit()
        return jsonify(product_info), HTTPStatus.CREATED
    except:
        #tratar possíveis erros no registro do produto
        {"erro":"Verifique sua requisição"}, HTTPStatus.BAD_REQUEST


@auth_partner.login_required
def update_product(product_id):
    session: Session = db.session()

    data = request.get_json()
    
    product = ProductModel.query.get(product_id)
    print(product)
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
    
    product: ProductModel = ProductModel.query.filter_by(id = product_id).first()

    return jsonify(product), HTTPStatus.OK

