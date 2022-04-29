from dataclasses import dataclass
from datetime import datetime
from flask_sqlalchemy import Model
from sqlalchemy import Column, String, Numeric, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from decimal import Decimal

@dataclass
class Product(Model):
    id: int
    name: str
    description: str
    starting_price: Decimal
    auction_start: datetime
    auction_end: datetime
    active: bool
    __tablename__ = "products"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(60), nullable=False)
    description = Column(String(1500), nullable=False)
    starting_price = Column(Numeric(asdecimal=True), nullable=False)
    auction_start = Column(DateTime)
    auction_end = Column(DateTime)
    active = Column(Boolean, nullable=False, default=False)
    id_partner = Column(UUID(as_uuid=True), ForeignKey("partners.id"), nullable=False)
