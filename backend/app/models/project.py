import datetime
from flask_pymongo import PyMongo
from bson import ObjectId  # Import to handle MongoDB ObjectIds

from app.utils.db import mongo
import uuid

class Project:
    @staticmethod
    def create_project(data):
        data["id"] = uuid.uuid4()
        data["created_at"] = datetime.datetime.now(datetime.timezone.utc)
        data["updated_at"] = datetime.datetime.now(datetime.timezone.utc)
        result = mongo.db.projects.insert_one(data)
        return {"_id": str(result.inserted_id)}  # Convert ObjectId to string

    @staticmethod
    def get_all_projects():
        projects = mongo.db.projects.find()
        return [Project.format_project(p) for p in projects]  # Format projects before returning

    @staticmethod
    def get_project_by_id(project_id):
        project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
        return Project.format_project(project) if project else None

    @staticmethod
    def update_project(project_id, data):
        data["updated_at"] = datetime.datetime.now(datetime.timezone.utc)
        mongo.db.projects.update_one({"_id": ObjectId(project_id)}, {"$set": data})
        updated_project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
        return Project.format_project(updated_project)

    @staticmethod
    def delete_project(project_id):
        mongo.db.projects.delete_one({"_id": ObjectId(project_id)})
        return {"message": "Project deleted successfully"}

    @staticmethod
    def format_project(project):
        """ Convert MongoDB document to a JSON-serializable format """
        return {
            "id": str(project["_id"]),
            "name": project.get("name"),
            "description": project.get("description"),
            "tags": project.get("tags", []),
            "status": project.get("status", "Unknown"),
            "created_at": project.get("created_at"),
            "updated_at": project.get("updated_at")
        }
