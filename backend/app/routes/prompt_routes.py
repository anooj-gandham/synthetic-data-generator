from flask import Blueprint
from app.controllers.prompt_controller import PromptController

# Define Blueprint for prompt routes
prompt_bp = Blueprint('prompt_bp', __name__)

# Define API routes
prompt_bp.add_url_rule('/prompts', view_func=PromptController.create_prompt, methods=['POST'])
prompt_bp.add_url_rule('/prompts', view_func=PromptController.get_prompts, methods=['GET'])
prompt_bp.add_url_rule('/prompts/<string:prompt_id>', view_func=PromptController.get_prompt, methods=['GET'])
prompt_bp.add_url_rule('/prompts/<string:prompt_id>', view_func=PromptController.update_prompt, methods=['PUT'])
prompt_bp.add_url_rule('/prompts/<string:prompt_id>', view_func=PromptController.delete_prompt, methods=['DELETE'])
