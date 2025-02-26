from app.models.prompt import Prompt

class PromptService:
    @staticmethod
    def create_prompt(data):
        return Prompt.create_prompt(data)

    @staticmethod
    def get_all_prompts():
        return Prompt.get_all_prompts()

    @staticmethod
    def get_prompt_by_id(prompt_id):
        return Prompt.get_prompt_by_id(prompt_id)

    @staticmethod
    def update_prompt(prompt_id, data):
        return Prompt.update_prompt(prompt_id, data)

    @staticmethod
    def delete_prompt(prompt_id):
        Prompt.delete_prompt(prompt_id)
