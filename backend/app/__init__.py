from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure MONGO_URI is set before initializing
    if not app.config.get("MONGO_URI"):
        raise ValueError("MONGO_URI is missing. Check your .env file.")

    # Initialize MongoDB
    mongo.init_app(app)

    # Register blueprints
    with app.app_context():
        from app.routes import data_routes
        app.register_blueprint(data_routes)

    return app
