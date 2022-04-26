from flask import Flask, Blueprint
from app.routes.user_routes import bp as bp_users
from app.routes.product_routes import bp as bp_products
from app.routes.partner_routes import bp as bp_partner
from app.routes.category_routes import bp as bp_category
from app.routes.bid_routes import bp as bp_bids

bp_api = Blueprint("api", __name__, url_prefix="/api")

def init_app(app: Flask):

    bp_partner.register_blueprint(bp_products)
    bp_partner.register_blueprint(bp_bids)

    bp_api.register_blueprint(bp_partner)
    bp_api.register_blueprint(bp_users)
    bp_api.register_blueprint(bp_category)

    app.register_blueprint(bp_api)