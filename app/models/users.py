from flask_sqlalchemy import Model
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class User(Model):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(60), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(12), nullable=False)
    birth_date = Column(Date, nullable=False)
    password_hash = Column(String(511), nullable=False)
    id_address = Column(UUID(as_uuid=True), ForeignKey("addresses.id"))
