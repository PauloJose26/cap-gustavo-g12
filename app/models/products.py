from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Column, String, Numeric, DateTime, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, backref
from uuid import uuid4
from decimal import Decimal
from app.config.database import db


@dataclass
class ProductModel(db.Model):
    id: str
    name: str
    description: str
    starting_price: Decimal
    auction_start: datetime
    auction_end: datetime
    active: bool
    partner_id = str
    task_id = str
    categories = list
    
    __tablename__ = "products"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(60), nullable=False)
    description = Column(String(1500), nullable=False)
    starting_price = Column(Numeric(asdecimal=True), nullable=False)
    auction_start = Column(DateTime)
    auction_end = Column(DateTime)
    active = Column(Boolean, default=False)
    task_id = Column(UUID(as_uuid=True), nullable=True, unique=True)
    partner_id = Column(UUID(as_uuid=True), ForeignKey("partners.id"), nullable=False)
    bids = relationship("BidModel", backref=backref("product", uselist=False))
    categories = relationship("CategorieModel", secondary="product_categorie")
    
    @classmethod
    def verify_data(cls, new_date: datetime):
        date_start = (cls.auction_start.year, cls.auction_start.month, cls.auction_start.day, cls.auction_start.hour, cls.auction_start.month, cls.auction_start.second)
        date_end = (cls.auction_end.year, cls.auction_end.month, cls.auction_end.day, cls.auction_end.hour, cls.auction_end.month, cls.auction_end.second)
        date = (new_date.year, new_date.month, new_date.day, new_date.hour, new_date.month, new_date.second)
        
        return date_start < date < date_end
    
