from flask import Flask
from flask_cors import CORS
from . import db


def create_app():
    app = Flask(__name__)
    CORS(app)
    db.init_app(app)
    return app


app = create_app()


@app.route("/events")
def home():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
