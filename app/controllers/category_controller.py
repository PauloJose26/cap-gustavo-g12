from flask import request, current_app, jsonify
from app.models.categories import CategorieModel
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

def get_categories():
    categories = (current_app.db.session.query(CategorieModel).all())

    serializer = [
        {
            "id": category.id,
            "name": category.name,
            "description": category.description
        } for category in categories
    ]
    
    return jsonify(serializer)


def get_category_by_id(category_id):
    category = current_app.db.session.query(CategorieModel).get(category_id)
    
    return jsonify(category)


def register_category():
    data = request.get_json()
    name = data["name"].capitalize()
    data["name"] = name

    
    new_category = CategorieModel(**data)
    try:
        current_app.db.session.add(new_category)
        current_app.db.session.commit()
        
        return jsonify(new_category), HTTPStatus.CREATED
    except IntegrityError:
        #UNIQUE CONSTRAINT NOT WORKING. MUST CORRECT.
        return {"erro": "Categoria já existente. Insira outro nome."}, HTTPStatus.CONFLICT
    
def patch_category(category_id):
    data = request.get_json()

    category = CategorieModel.query.get(category_id)

    
    for key, value in data.items():
        setattr(category, key, value.capitalize())
    
    
    try:
        current_app.db.session.add(category)
        current_app.db.session.commit()

        return jsonify(category)
    except IntegrityError:
        {"erro": "Categoria já existente. Insira outro nome."}, HTTPStatus.CONFLICT
        
def delete_category(category_id):
    query = CategorieModel.query.get(category_id)

    current_app.db.session.delete(query)
    current_app.db.session.commit()

    return {"sucesso":"A categoria foi removida com sucesso"}, HTTPStatus.OK