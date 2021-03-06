from dataclasses import dataclass
from flask_sqlalchemy import Model
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.config.database import db
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class PartnerModel(db.Model):
    id: str
    name: str
    email: str
    cnpj: str
    phone_number: str
    about: str
    __tablename__ = "partners"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(60), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    cnpj = Column(String(14), nullable=False, unique=True)
    phone_number = Column(String(12), nullable=False)
    about = Column(String(500))
    id_address = Column(UUID(as_uuid=True), ForeignKey("addresses.id"))
    password_hash = Column(String(511), nullable=True)
    api_key= Column(String)
    role= Column(String)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
