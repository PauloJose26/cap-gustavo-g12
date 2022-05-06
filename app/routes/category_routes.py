from flask import Blueprint
from app.controllers import category_controller

bp = Blueprint("categories", __name__, url_prefix="/categories")

bp.post("")(category_controller.register_category)
bp.get("")(category_controller.get_categories)
bp.get("/<category_id>")(category_controller.get_category_by_id)
bp.patch("/<category_id>")(category_controller.patch_category)
bp.delete("/<category_id>")(category_controller.delete_category)
