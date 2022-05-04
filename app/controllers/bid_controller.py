from app.models import BidModel, ProductModel, UserModel
from app.config.database import db
from app.exceptions import BidsError

from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.orm import Session
from datetime import datetime, timedelta


def register_bid():
    date = datetime.now()
    data: dict = request.get_json()
    data = { key: value for key, value in data.items if key in BidModel.keys_valid }
    if not data.get("user_id") or not data.get("product_id") or not data.get("price"):
        raise BidsError({ "error": "Chaves insuficiente", "chaves": [ "price", "user_id" ] })
    
    session: Session = db.session
    product: ProductModel = session.query(ProductModel).get(data["product_id"])
    user: UserModel = session.query(UserModel).get(data["user_id"])
    
    if not product or not user:
        raise BidsError({ "error": "Produtos não encontrado" })
    if product.active and product.verify_data(date):
        raise BidsError({ "error": "Fora do  prazo do leilão" })
    
    bid = BidModel(**data)
    bids:list[BidModel] = session.query(BidModel).join(ProductModel.id == BidModel.id_product).order_by(BidModel.price).all().reverse()
    if bid.price <  bids[0].price * 1.1:
        raise BidsError({ "error": "O preço precisa estar acima de 10% do preco anterior" })
    
    if product.auction_end.minute - date.minute <= 2:
        setattr(product, "auction_end", product.auction_end + timedelta(minutes=1))
    
    session.add(bid)
    session.commit()
    
    return jsonify(bid), HTTPStatus.OK
