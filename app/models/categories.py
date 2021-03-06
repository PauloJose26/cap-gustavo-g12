from dataclasses import dataclass
from flask_sqlalchemy import Model
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.config.database import db

@dataclass
class CategorieModel(db.Model):
    name: str
    description: str
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(60), unique=True, nullable=False)
    description = Column(String(1500), nullable=False)
