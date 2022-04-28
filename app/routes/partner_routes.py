from flask import Blueprint
from app.controllers import partner_controller

bp = Blueprint("partners", __name__, url_prefix="/partners")

bp.get("")(partner_controller.get_partners)
bp.get("/<int:partner_id>")(partner_controller.get_partner_by_id)