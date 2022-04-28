from flask_sqlalchemy import Model
from sqlalchemy import Column, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Bid(Model):
    __tablename__ = "bids"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    price = Column(Numeric(asdecimal=True), nullable=False)
    id_user = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    id_product = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
