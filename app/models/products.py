from flask_sqlalchemy import Model
from sqlalchemy import Column, String, Numeric, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Product(Model):
    __tablename__ = "products"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(60), nullable=False)
    description = Column(String(1500), nullable=False)
    starting_price = Column(Numeric(asdecimal=True), nullable=False)
    auction_start = Column(DateTime)
    auction_end = Column(DateTime)
    active = Column(Boolean, nullable=False, default=True)
    id_partner = Column(UUID(as_uuid=True), ForeignKey("partners.id"), nullable=False)
