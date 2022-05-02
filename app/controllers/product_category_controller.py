from flask import session
from http import HTTPStatus
from flask import request, jsonify
from app.config.database import db
from sqlalchemy.orm.session import Session
from app.controllers.category_controller import register_category
from app.controllers.product_controller import register_product
from app.models.product_categorie import ProductCategorieModel


def register_product_category():
    
    session: Session = db.session()

    data = request.get_json()

    category = register_category(data["category"])
    data.pop("category")
    data["id_categorie"] = category.id
    #precisa do controller dos produtos para funcionar 
    product = register_product(data["product"])
    data.pop("product")
    data["id_product"] = product.id

    product_category = ProductCategorieModel(**data)

    session.add(product_category)
    session.commit()

    return jsonify(product_category), HTTPStatus.CREATED