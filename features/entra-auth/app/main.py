from flask import Flask, request, jsonify
from auth_config import require_auth
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", static_url_path="")

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")

@app.route("/chat", methods=["POST"])
@require_auth
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    headers = {
        "api-key": AZURE_OPENAI_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(
        f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2024-03-01-preview",
        headers=headers,
        json=payload
    )

    return jsonify(response.json())

@app.get("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)
