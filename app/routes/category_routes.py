from flask import Blueprint
from app.controllers import category_controller

bp = Blueprint("categories", __name__, url_prefix="/categories")

bp.post("")(category_controller.register_category)
bp.get("")(category_controller.get_categories)
bp.get("/<int:category_id>")(category_controller.get_category_by_id)
bp.patch("/<int:category_id>")(category_controller.patch_category)
bp.delete("/<int:category_id>")(category_controller.delete_category)
