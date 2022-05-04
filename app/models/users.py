from dataclasses import dataclass
from datetime import date
from flask_sqlalchemy import Model
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.config.database import db
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class UserModel(db.Model):
    id: int
    name: str
    cpf: str
    email: str
    phone_number: str
    birth_date: date
    api_key: str
    role: str

    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(60), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(12), nullable=False)
    birth_date = Column(Date, nullable=False)
    password_hash = Column(String(511), nullable=True)
    id_address = Column(UUID(as_uuid=True), ForeignKey("addresses.id"))
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