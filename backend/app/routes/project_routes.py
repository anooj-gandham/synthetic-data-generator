from flask import Blueprint
from app.controllers.project_controller import ProjectController

# Define Blueprint for project routes
project_bp = Blueprint('project_bp', __name__)

# Define API routes
project_bp.add_url_rule('/projects', view_func=ProjectController.create_project, methods=['POST'])
project_bp.add_url_rule('/projects', view_func=ProjectController.get_projects, methods=['GET'])
project_bp.add_url_rule('/projects/<string:project_id>', view_func=ProjectController.get_project, methods=['GET'])
project_bp.add_url_rule('/projects/<string:project_id>', view_func=ProjectController.update_project, methods=['PUT'])
project_bp.add_url_rule('/projects/<string:project_id>', view_func=ProjectController.delete_project, methods=['DELETE'])
