from app.config import celery

celery = celery.create_celery_app()

