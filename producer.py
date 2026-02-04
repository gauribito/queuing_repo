from app.tasks import process_order

if __name__ == "__main__":
    for i in range(5):
        result = process_order.delay(i)
        print(f"Queued order {i}, task id: {result.id}")
