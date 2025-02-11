#!/bin/bash

# Set the base directory for the project
BASE_DIR="./backend"

# Create directories
declare -a dirs=(
    "$BASE_DIR/app"
    "$BASE_DIR/app/controllers"
    "$BASE_DIR/app/models"
    "$BASE_DIR/app/routes"
    "$BASE_DIR/app/services"
    "$BASE_DIR/app/utils"
    "$BASE_DIR/tests"
)

for dir in "${dirs[@]}"; do
    mkdir -p "$dir"
done

# Create files with boilerplate content

# run.py
cat << 'EOF' > "$BASE_DIR/run.py"
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF

# app/__init__.py
cat << 'EOF' > "$BASE_DIR/app/__init__.py"
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
EOF

# app/config.py
cat << 'EOF' > "$BASE_DIR/app/config.py"
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/your_db_name")
EOF

# app/controllers/__init__.py
touch "$BASE_DIR/app/controllers/__init__.py"

# app/controllers/project_controller.py
cat << 'EOF' > "$BASE_DIR/app/controllers/project_controller.py"
from flask import request, jsonify
from app.services.project_service import ProjectService

class ProjectController:
    @staticmethod
    def create_project():
        data = request.get_json()
        project = ProjectService.create_project(data)
        return jsonify(project), 201

    @staticmethod
    def get_projects():
        projects = ProjectService.get_all_projects()
        return jsonify(projects), 200

    @staticmethod
    def get_project(project_id):
        project = ProjectService.get_project_by_id(project_id)
        return jsonify(project), 200

    @staticmethod
    def update_project(project_id):
        data = request.get_json()
        project = ProjectService.update_project(project_id, data)
        return jsonify(project), 200

    @staticmethod
    def delete_project(project_id):
        ProjectService.delete_project(project_id)
        return '', 204
EOF

# app/models/__init__.py
touch "$BASE_DIR/app/models/__init__.py"

# app/models/project.py
cat << 'EOF' > "$BASE_DIR/app/models/project.py"
from flask_pymongo import PyMongo

mongo = PyMongo()

class Project:
    @staticmethod
    def create_project(data):
        project_id = mongo.db.projects.insert_one(data).inserted_id
        return str(project_id)

    @staticmethod
    def get_all_projects():
        return list(mongo.db.projects.find({}, {"_id": 0}))

    @staticmethod
    def get_project_by_id(project_id):
        return mongo.db.projects.find_one({"_id": project_id}, {"_id": 0})

    @staticmethod
    def update_project(project_id, data):
        mongo.db.projects.update_one({"_id": project_id}, {"$set": data})
        return mongo.db.projects.find_one({"_id": project_id}, {"_id": 0})

    @staticmethod
    def delete_project(project_id):
        mongo.db.projects.delete_one({"_id": project_id})
EOF

# app/routes/__init__.py
cat << 'EOF' > "$BASE_DIR/app/routes/__init__.py"
from flask import Blueprint
from app.controllers.project_controller import ProjectController

def register_routes(app):
    project_bp = Blueprint('project_bp', __name__)

    project_bp.add_url_rule('/projects', view_func=ProjectController.create_project, methods=['POST'])
    project_bp.add_url_rule('/projects', view_func=ProjectController.get_projects, methods=['GET'])
    project_bp.add_url_rule('/projects/<string:project_id>', view_func=ProjectController.get_project, methods=['GET'])
    project_bp.add_url_rule('/projects/<string:project_id>', view_func=ProjectController.update_project, methods=['PUT'])
    project_bp.add_url_rule('/projects/<string:project_id>', view_func=ProjectController.delete_project, methods=['DELETE'])

    app.register_blueprint(project_bp, url_prefix='/api')
EOF

# app/services/__init__.py
touch "$BASE_DIR/app/services/__init__.py"

# app/services/project_service.py
cat << 'EOF' > "$BASE_DIR/app/services/project_service.py"
from app.models.project import Project

class ProjectService:
    @staticmethod
    def create_project(data):
        return Project.create_project(data)

    @staticmethod
    def get_all_projects():
        return Project.get_all_projects()

    @staticmethod
    def get_project_by_id(project_id):
        return Project.get_project_by_id(project_id)

    @staticmethod
    def update_project(project_id, data):
        return Project.update_project(project_id, data)

    @staticmethod
    def delete_project(project_id):
        Project.delete_project(project_id)
EOF

# app/utils/__init__.py
touch "$BASE_DIR/app/utils/__init__.py"

# app/utils/db.py
cat << 'EOF' > "$BASE_DIR/app/utils/db.py"
from flask_pymongo import PyMongo

mongo = PyMongo()

def initialize_db(app):
    mongo.init_app(app)
EOF

# tests/__init__.py
touch "$BASE_DIR/tests/__init__.py"

# tests/test_project.py
cat << 'EOF' > "$BASE_DIR/tests/test_project.py"

import unittest
from app import create_app

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config["MONGO_URI"] = "mongodb://localhost:27017/test_db"

    def test_create_project(self):
        response = self.client.post('/api/projects', json={
            'name': 'Test Project',
            'description': 'A test project',
            'tags': ['test', 'project']
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
EOF

# .env
cat << 'EOF' > "$BASE_DIR/.env"
SECRET_KEY=your_secret_key
MONGO_URI=mongodb://localhost:27017/your_db_name
EOF

# requirements.txt
cat << 'EOF' > "$BASE_DIR/requirements.txt"
Flask==2.1.1
pymongo==4.3.3
dnspython==2.3.0
flask_pymongo==2.3.0
python-dotenv==0.20.0
EOF

# Dockerfile
cat << 'EOF' > "$BASE_DIR/Dockerfile"
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=run.py

CMD ["flask", "run", "--host=0.0.0.0"]
EOF

# docker-compose.yml
cat << 'EOF' > "$BASE_DIR/docker-compose.yml"
version: '3.8'

services:
  web:
    build: .
    container_name: flask_app
    ports:
      - "5000:5000"
    environment:
      - MONGO_URI=mongodb://mongo:27017/your_db_name
    depends_on:
      - mongo

  mongo:
    image: mongo:latest
    container_name: mongo_db
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
EOF

# .dockerignore
cat << 'EOF' > "$BASE_DIR/.dockerignore"
__pycache__
*.pyc
.env
.venv
.git
.DS_Store
EOF

# .gitignore
cat << 'EOF' > "$BASE_DIR/.gitignore"
__pycache__/
*.pyc
.env
.venv/
.git/
.DS_Store
EOF

echo "Flask-MongoDB boilerplate with improved structure inspired by Apache Airflow created!"
echo "Navigate to the 'flask_mongo_app' directory and start developing."
echo "To run the application with Docker, use: docker-compose up --build"

