from flask import request, current_app, jsonify
from app.models.categories import CategorieModel
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

def get_categories():
    categories = (current_app.db.session.query(CategorieModel).all())

    serializer = [
        {
            "name": category.name,
            "description": category.description
        } for category in categories
    ]
    
    return jsonify(serializer)


def get_category_by_id(category_id):
    category = current_app.db.sesson.query(CategorieModel).get(category_id)
    
    return jsonify(category)


def register_category():
    data = request.get_json()
    name = data["name"].capitalize()
    data["name"] = name

    
    new_category = CategorieModel(**data)
    try:
        current_app.db.session.add(new_category)
        current_app.db.commit()
        
        return jsonify(new_category), HTTPStatus.CREATED
    except IntegrityError:
        return {"erro": "Categoria já existente no sistema"}, HTTPStatus.CONFLICT
    