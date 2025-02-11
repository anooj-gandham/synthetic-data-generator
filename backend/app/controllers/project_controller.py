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
