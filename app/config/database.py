from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQL_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.db = db

    from app.models.addresses import AddressModel
    from app.models.bids import BidModel
    from app.models.categories import CategorieModel
    from app.models.partners import PartnerModel
    from app.models.product_categorie import ProductCategorieModel
    from app.models.products import ProductModel
    from app.models.users import UserModel

    return app