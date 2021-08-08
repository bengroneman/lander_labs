from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/events")
def home():
    return "<p>Hello, World!</p>"