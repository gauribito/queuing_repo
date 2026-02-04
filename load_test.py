from app.tasks import process_order

for i in range(100):
    process_order.delay(i)
    print("Queued:", i)
