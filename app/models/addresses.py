from flask_sqlalchemy import Model
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Address(Model):
    __tablename__ = "addresses"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    country = Column(String(20), nullable=False)
    state = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    street = Column(String(60), nullable=False)
    number = Column(String(10), nullable=False)
    complement = Column(String(300))
    postal_code = Column(String(8), nullable=False)
