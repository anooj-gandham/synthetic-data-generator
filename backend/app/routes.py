from flask import Blueprint, request, jsonify
from app.generator import SyntheticDataGenerator
from app.deduplicator import DataDeduplicator

data_routes = Blueprint('data_routes', __name__)

# Initialize generator and deduplicator
generator = SyntheticDataGenerator()
deduplicator = DataDeduplicator()

@data_routes.route('/generate', methods=['POST'])
def generate_data():
    data = request.json
    sample_prompts = data.get('sample_prompts', [])
    system_prompt = data.get('system_prompt', '')
    num_prompts = data.get('num_prompts', 10)

    synthetic_prompts = generator.generate_batch(
        sample_prompts=sample_prompts,
        system_prompt=system_prompt,
        num_prompts=num_prompts
    )

    return jsonify({"synthetic_prompts": synthetic_prompts.model_dump()})
