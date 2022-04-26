from flask import Blueprint
from app.controllers import product_controller

bp = Blueprint("products", __name__, url_prefix="/products")

bp.post("")(product_controller.register_product)
bp.patch("/<int:product_id>")(product_controller.update_product)
bp.get("")(product_controller.get_products)
bp.get("/<int:product_id>")(product_controller.get_product_by_id)