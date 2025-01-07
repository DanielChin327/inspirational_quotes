# Backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def test():
    return "Routes are working"

@app.route('/api/quote')
def get_quote():
    """Fetch a random quote from ZenQuotes and return it."""
    try:
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch quote", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)