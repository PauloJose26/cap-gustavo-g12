from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint("users", __name__, url_prefix="/users")

bp.post("")(user_controller.register_user)
bp.patch("/<int:user_id>")(user_controller.update_user)
bp.delete("/<int:user_id>")(user_controller.delete_user)
bp.get("")(user_controller.get_user)
bp.get("/<int:user_id>")(user_controller.get_user_by_id)