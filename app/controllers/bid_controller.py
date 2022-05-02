from app.models import BidModel, ProductModel, UserModel
from app.config.database import db

from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.orm import Session


def register_bid():
    data: dict = request.get_json()
    data = { key: value for key, value in data.items if key in BidModel.keys_valid }
    
    if not data.get("user_id") or not data.get("product_id") or not data.get("price"):
        ...
    
    session: Session = db.session
    product = session.query(ProductModel).get(data["product_id"])
    user = session.query(UserModel).get(data["user_id"])
    
    if not product or not user:
        ...
    
    bid = BidModel(**data)
    session.add(bid)
    session.commit()
    
    return jsonify(bid), HTTPStatus.OK
