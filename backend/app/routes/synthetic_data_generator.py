from flask import Blueprint, request, jsonify
from app.utils.prompts_generator.synthetic_v1 import SyntheticDataGenerator

# Create a Flask Blueprint
synthetic_bp = Blueprint("synthetic", __name__)

@synthetic_bp.route("/generate_synthetic_data", methods=["GET"])
def generate_synthetic_data():
    """API endpoint to call SyntheticDataGenerator."""
    
    # Initialize the generator
    generator = SyntheticDataGenerator()

    samples = """
Phone starts off flat. It then starts rotating slowly and makes a quick round, then slows down and stops. This happens while the phone is levitating. (Total: ~7s)
Card shoots up, does backflips multiple times, and slowly comes back down in a diagonal pose to highlight the depth. (Total: ~9s)
Shoe does a running animation of jumping up and down at the same place, like someone is wearing it. The motion speeds up slightly before slowing down again. (Total: ~7s)
Shoe makes a couple of rotations and stands on its toe at an angle, highlighting all the aspects of the shoe. (Total: ~5s)
Shoe does cartwheels (5s), then makes a big jump, does multiple flips (4s), and lands on the heel in a perfect pose (3s). (Total: ~14s)
Sunscreen rotates (5s) while slowly coming into focus on the left part of the screen (3s). (Total: ~8s)
Phone rotates slowly (4s), revealing its screen with a smooth transition. (Total: ~4s)
Phone races to a vertical distance very fast and then moves and rotates very slowly, like in slow motion (10s), highlighting the phone's speed. (Total: ~12s)
"""
    system_prompt = "You are a marketing person. You are tasked to create a marketing campain to increase the sales of mibile phones. You have a tool at your disposal using which phone advertisement videos can be created using simple text prompts. The text input to this tool should describe only the animation of the phone and no other details. Using the below prompts as few examples, please generate more prompts which I can use with my tool."
    synthetic_prompts = generator.generate_batch(samples, system_prompt, 4)
    
    return jsonify({"prompts": synthetic_prompts}), 200
