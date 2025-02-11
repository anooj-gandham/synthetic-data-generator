from flask import Flask
from .config import Config
from .utils.db import initialize_db
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    initialize_db(app)
    register_routes(app)

    return app
