from celery import Celery
import time
import random

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 3})
def process_order(self, order_id):
    time.sleep(2)
    if random.choice([True, False]):
        raise Exception("Random processing failure")
    return f"Order {order_id} processed successfully"
