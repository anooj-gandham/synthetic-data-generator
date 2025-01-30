from bson.objectid import ObjectId
from . import mongo

collection = mongo.db.prompts

def create_prompt(prompt_text, metadata=None):
    """Create a new prompt entry in the database"""
    data = {"prompt_text": prompt_text, "metadata": metadata or {}}
    result = collection.insert_one(data)
    return {"message": "Prompt added", "id": str(result.inserted_id)}

def get_prompt(prompt_id):
    """Retrieve a single prompt by ID"""
    prompt = collection.find_one({"_id": ObjectId(prompt_id)}, {"_id": 0})  # Exclude _id from output
    return prompt or {"error": "Prompt not found"}

def get_all_prompts():
    """Retrieve all prompts from the collection"""
    return list(collection.find({}, {"_id": 0}))  # Exclude _id from output

def update_prompt(prompt_id, new_prompt_text):
    """Update a prompt's text by ID"""
    result = collection.update_one(
        {"_id": ObjectId(prompt_id)}, {"$set": {"prompt_text": new_prompt_text}}
    )
    return {"message": "Updated successfully" if result.modified_count else "No changes made"}

def delete_prompt(prompt_id):
    """Delete a prompt by ID"""
    result = collection.delete_one({"_id": ObjectId(prompt_id)})
    return {"message": "Deleted successfully" if result.deleted_count else "Prompt not found"}