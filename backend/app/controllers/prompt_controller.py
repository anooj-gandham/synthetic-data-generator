from flask import request, jsonify
from app.services.prompt_service import PromptService

class PromptController:
    @staticmethod
    def create_prompt():
        data = request.get_json()
        prompt = PromptService.create_prompt(data)
        return jsonify(prompt), 201

    @staticmethod
    def get_prompts():
        prompts = PromptService.get_all_prompts()
        return jsonify(prompts), 200

    @staticmethod
    def get_prompt(prompt_id):
        prompt = PromptService.get_prompt_by_id(prompt_id)
        return jsonify(prompt), 200

    @staticmethod
    def update_prompt(prompt_id):
        data = request.get_json()
        prompt = PromptService.update_prompt(prompt_id, data)
        return jsonify(prompt), 200

    @staticmethod
    def delete_prompt(prompt_id):
        PromptService.delete_prompt(prompt_id)
        return '', 204
