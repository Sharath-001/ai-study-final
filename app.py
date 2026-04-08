from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "running"

@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({
        "status": "ok",
        "observation": {}
    })

@app.route("/infer", methods=["POST"])
def infer():
    data = request.get_json()
    topic = data.get("topic", "General Topic")

    return jsonify({
        "response": f"Explanation of {topic}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)