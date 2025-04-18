from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Azure OpenAI configuration
AZURE_OPENAI_API_URL = "https://chatbotai5951744364.openai.azure.com/openai/deployments/gpt-35-turbo-16k/chat/completions?api-version=2025-01-01-preview"
AZURE_OPENAI_API_KEY = "5frwJaPjy7Mmjgc4wiYur2bjMAsIlDCx5cjTpG3HJIrZDyC3EyfCJQQJ99BDACHYHv6XJ3w3AAAAACOGn0Ke"
MODEL_NAME = "gpt-35-turbo-16k"
# Load from environment variable

# Welcome route for testing
@app.route('/')
def index():
    return "✅ AI Chatbot API is running. Send a POST request to /get_response with JSON: {\"message\": \"Hello\"}"

# Chatbot response handler
def get_bot_response(user_message):
    headers = {
        "api-key": AZURE_OPENAI_API_KEY,
        "Content-Type": "application/json",
        "x-ms-model-mesh-model-name": MODEL_NAME,
    }
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        'temperature' :0.8
    }
    try:
        response = requests.post(AZURE_OPENAI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error communicating with Azure OpenAI API: {e}"

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data.get('message')
    print(data, flush=True)
    bot_reply = get_bot_response(user_message)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
