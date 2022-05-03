from tasks import celery

@celery.task
def close_auction(product_id):
    ...