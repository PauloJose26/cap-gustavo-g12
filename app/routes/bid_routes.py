from flask import Blueprint
from app.controllers import bid_controller

bp = Blueprint("bids", __name__, url_prefix="/bids")

bp.post("")(bid_controller.register_bid)