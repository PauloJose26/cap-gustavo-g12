from dataclasses import dataclass
from flask_sqlalchemy import Model
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

@dataclass
class ProductCategorie(Model):
    id: int
    id_product: int
    id_categorie: int
    __tablename__ = "product_categorie"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id_product = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    id_categorie = Column(UUID(as_uuid=True), ForeignKey("categories.id"))
