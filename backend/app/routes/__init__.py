from flask import Flask
from .project_routes import project_bp
from .prompt_routes import prompt_bp
from .synthetic_data_generator import synthetic_bp

def register_routes(app: Flask):
    app.register_blueprint(project_bp, url_prefix='/api')  # Register project routes
    app.register_blueprint(prompt_bp, url_prefix='/api')  # Register prompt routes
    app.register_blueprint(synthetic_bp, url_prefix='/api')  # Register synthetic data generator routes