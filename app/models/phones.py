from flask_sqlalchemy import Model
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Phone(Model):
    __tablename__ = "phones"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    country_code = Column(String, nullable=False)
    number = Column(String, nullable=False)
