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

load_dotenv()

def register_product():
    from app.tasks import close_auction, open_auction

    session: Session = db.session()

    data:dict = request.get_json()

    partner_id = "e5a4ab88-73ce-444b-b672-2f1bfa549e7c" #MOCK. Fazer autenticação.

    data["partner_id"] = partner_id
    
    open_time = datetime.strptime(data["auction_start"], "%Y-%m-%d %H:%M") - datetime.now()
    close_time = datetime.strptime(data["auction_end"], "%Y-%m-%d %H:%M") - datetime.now()
    
    if open_time.seconds <= 60:
        return {"erro": "A data de início do leilão deve ser de no mínimo 1 minuto à partir do horário atual"}, HTTPStatus.NOT_ACCEPTABLE
    
    if close_time.seconds > os.getenv('CLOSE_TIME'):
        return {"erro": "O tempo máximo de duração do leilão é de 24 horas." }, HTTPStatus.NOT_ACCEPTABLE
    
    
    
    try:
        
        if data.get("categories"):
            for i in data["categories"]:
                product_category = session.query(CategorieModel).filter_by(name = i).first()
                if product_category:
                    product_info.categories.append(product_category)
        
        product_info = ProductModel(**data)
        
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
