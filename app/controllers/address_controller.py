from flask import jsonify
from app.config.database import db
from sqlalchemy.orm.session import Session
from app.models.addresses import AddressModel

def register_address(address):
    session: Session = db.session()

    address_info = AddressModel(**address)

    session.add(address_info)

    session.commit()

    return address_info