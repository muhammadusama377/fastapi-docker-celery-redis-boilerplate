from celery import Celery

from .conf import settings

app = Celery(
    "tasks",
    broker=settings.celery_broker_url,
    backend=settings.celery_backend_url,
)
