from dataclasses import dataclass, asdict
from datetime import datetime
from math import prod
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
    partner_id: str
    task_id: str
    categories: list
    
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
    def verify_data(cls, new_date: datetime, date_start: datetime, date_end: datetime):
        date_start_tuple = (date_start.year, date_start.month, date_start.day, date_start.hour, date_start.month, date_start.second)
        date_end_tuple = (date_end.year, date_end.month, date_end.day, date_end.hour, date_end.month, date_end.second)
        date = (new_date.year, new_date.month, new_date.day, new_date.hour, new_date.month, new_date.second)
        print(date_start_tuple)
        return date >= date_start_tuple and date < date_end_tuple
