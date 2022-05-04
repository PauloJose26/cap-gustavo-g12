from signal import pause
from tasks import celery
from datetime import datetime
from app.config.database import db
from app.models.products import ProductModel
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query

@celery.task
def close_auction(product_id, auction_end):
    pause(datetime(auction_end))
    
    session: Session = db.session()
    product: Query = session.query(ProductModel).get(product_id)
    
    setattr(product, "active", False)
    