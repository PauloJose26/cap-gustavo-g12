from dataclasses import dataclass
from flask_sqlalchemy import Model
from sqlalchemy import Column, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from decimal import Decimal
from app.config.database import db

@dataclass
class BidModel(db.Model):
    keys_valid = [ "user_id", "product_id", "price" ]
    
    id: int
    price: Decimal
    __tablename__ = "bids"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    price = Column(Numeric(asdecimal=True), nullable=False)
    id_user = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    id_product = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
