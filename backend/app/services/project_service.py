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
