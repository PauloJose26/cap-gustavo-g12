from time import sleep
from app.config import celery


import pause
# from app.tasks import celery_init
from datetime import datetime
from app.config.database import db
from app.models.products import ProductModel
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query

celery_init = celery.create_celery_app()



@celery_init.task()
def close_auction(product_id, auction_end):
    print(celery_init)
    print("Task iniciada, dormindo >>>")
    
    sleep(auction_end)
    
    session: Session = db.session()
    product: Query = session.query(ProductModel).get(product_id)
    
    print("Task completada")
    
    setattr(product, "active", False)

@celery_init.task()
def open_auction(product_id, auction_start):
    print("Task iniciada, dormindo >>>")
    
    sleep(auction_start)
    
    session: Session = db.session()
    product: Query = session.query(ProductModel).get(product_id)
    
    setattr(product, "active", True)