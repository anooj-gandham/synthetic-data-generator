import datetime
from flask_pymongo import PyMongo
from bson import ObjectId
import numpy as np

from app.utils.db import mongo

class Prompt:
    @staticmethod
    def create_prompt(data):
        data["created_at"] = datetime.datetime.now(datetime.timezone.utc)
        data["updated_at"] = datetime.datetime.now(datetime.timezone.utc)
        result = mongo.db.prompts.insert_one(data)
        return {"_id": str(result.inserted_id)}  

    @staticmethod
    def get_all_prompts():
        prompts = mongo.db.prompts.find()
        return [Prompt.format_prompt(p) for p in prompts]

    @staticmethod
    def get_prompt_by_id(prompt_id):
        prompt = mongo.db.prompts.find_one({"_id": ObjectId(prompt_id)})
        return Prompt.format_prompt(prompt) if prompt else None

    @staticmethod
    def update_prompt(prompt_id, data):
        data["updated_at"] = datetime.datetime.now(datetime.timezone.utc)
        mongo.db.prompts.update_one({"_id": ObjectId(prompt_id)}, {"$set": data})
        updated_prompt = mongo.db.prompts.find_one({"_id": ObjectId(prompt_id)})
        return Prompt.format_prompt(updated_prompt)

    @staticmethod
    def delete_prompt(prompt_id):
        mongo.db.prompts.delete_one({"_id": ObjectId(prompt_id)})
        return {"message": "Prompt deleted successfully"}

    @staticmethod
    def get_all_embeddings() -> np.ndarray:
        """Retrieve all embeddings from prompts and return them as a NumPy array."""
        prompts = mongo.db.prompts.find({}, {"embeddings": 1})  # Fetch only embeddings field
        embeddings = [p.get("embeddings") for p in prompts if "embeddings" in p and p["embeddings"]]

        # Convert to NumPy array for efficient computation
        print("Embeddings Shape:", np.array(embeddings).shape)
        return np.array(embeddings)

    @staticmethod
    def format_prompt(prompt):
        """ Convert MongoDB document to a JSON-serializable format """
        return {
            "id": str(prompt["_id"]),
            "content": prompt.get("content"),
            "project": prompt.get("project"),
            # "embeddings": prompt.get("embeddings", []),
            "tags": prompt.get("tags", []),
            "created_at": prompt.get("created_at"),
            "updated_at": prompt.get("updated_at")
        }
