from celery import Celery
import time

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def process_order(order_id):
    time.sleep(2)
    return f"Order {order_id} processed"
