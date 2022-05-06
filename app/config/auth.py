from flask_httpauth import HTTPTokenAuth
from app.models.users import UserModel
from app.models.partners import PartnerModel
from app.config.database import db

auth_user = HTTPTokenAuth()

@auth_user.verify_token
def verify_token(api_key: str):
    user = UserModel.query.filter_by(api_key=api_key).first()
    if user:
        return user
    

@auth_user.get_user_roles
def get_user_roles(user):
    return user.role


auth_partner = HTTPTokenAuth()

@auth_partner.verify_token
def verify_token_papartner(api_key: str):
    partner = db.session.query(PartnerModel).filter_by(api_key=api_key).first()
    
    if partner:
        return partner

