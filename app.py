
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

VK_CONFIRMATION_CODE = "4fabf227"
VK_GROUP_ID = 180235186


@app.route("/")
def home():
    return jsonify({
        "status": "working",
        "message": "VK Goals Bot test server is alive!"
    })


@app.route("/health")
def health():
    return jsonify({"status": "OK"}), 200


@app.route("/vk-callback", methods=["POST"])
def vk_callback():
    data = request.get_json(silent=True)

    if not data:
        return "Invalid request", 400

    if data.get("group_id") != VK_GROUP_ID:
        return "Invalid group", 403

    event_type = data.get("type")

    if event_type == "confirmation":
        return VK_CONFIRMATION_CODE, 200, {
            "Content-Type": "text/plain"
        }

    return "ok", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
