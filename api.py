from flask import Flask, request, jsonify
from app.tasks import process_order

app = Flask(__name__)

@app.route("/enqueue", methods=["POST"])
def enqueue_task():
    data = request.json
    order_id = data.get("order_id")
    result = process_order.delay(order_id)
    return jsonify({
        "message": "Task queued",
        "task_id": result.id
    })

if __name__ == "__main__":
    app.run(port=5000)
