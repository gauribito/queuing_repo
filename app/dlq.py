failed_tasks = []

def send_to_dlq(task_id, reason):
    failed_tasks.append({
        "task_id": task_id,
        "reason": reason
    })
