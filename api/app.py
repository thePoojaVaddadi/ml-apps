from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

MODEL_PATH = "models/model.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

model = load_model()

@app.route("/")
def home():
    return jsonify({
        "message": "House Price MLOps API 🚀",
        "status": "running"
    })

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = [
        data["size"],
        data["bedrooms"],
        data["age"]
    ]

    prediction = model.predict([features])[0]

    return jsonify({
        "predicted_price": round(float(prediction), 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)