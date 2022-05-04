from flask_httpauth import HTTPTokenAuth
from app.models.users import UserModel

auth = HTTPTokenAuth()

@auth.verify_token
def verify_token(api_key: str):
    user = UserModel.query.filter_by(api_key=api_key).first()

    return user

@auth.get_user_roles
def get_user_roles(user):
    return user.role