from celery.result import AsyncResult
from app.tasks import celery_app

def check_status(task_id):
    result = AsyncResult(task_id, app=celery_app)
    print("Status:", result.status)
    if result.ready():
        print("Result:", result.result)

if __name__ == "__main__":
    task_id = input("Enter task id: ")
    check_status(task_id)
