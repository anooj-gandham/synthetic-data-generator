import gradio as gr
import requests

API_URL = "http://127.0.0.1:5000/generate"

def generate_data_ui(sample_prompts, system_prompt, num_prompts, llm_name):
    payload = {
        "sample_prompts": sample_prompts.split("\n"),
        "system_prompt": system_prompt,
        "num_prompts": int(num_prompts),
        "llm_name": llm_name,
    }
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        # print(response.json().get("synthetic_data"))
        return "\n".join(response.json().get("synthetic_prompts").get("prompts"))
    else:
        return f"Error: {response.text}"
 
def gradio_ui():
    with gr.Blocks() as app:
        gr.Markdown("### Synthetic Data Generator with LLM Selection")

        system_prompt_placeholder = """You are a marketing person. You are tasked to create a marketing campain to increase the sales of mobile phones. You have a tool at your disposal using which phone advertisement videos can be created using simple text prompts. The prompt should explain only the motion of the mobile phone. Using the below prompts as few examples, please generate more prompts which I can use with my tool."""

        sample_prompts_placeholder = """Phone start rotating slowly & followed by a more dramatic rotation and finally rotation ends slowly after completing 2 rounds at the origin. Duration is 7 seconds.
Phone travels to the side while rotating. duration 7 seconds
Phone oscillates just above the podium maintaining the centre position and rotates from left to right. Animation continues for 7 seconds
Phone tilts back and forth while positioned at the origin. duration 7 seconds"""

        sample_prompts = gr.Textbox(label="Sample Data Points", placeholder="Enter sample data points, one per line", value=sample_prompts_placeholder, lines=5)
        system_prompt = gr.Textbox(label="System Prompt", placeholder="Describe the type of data to generate", value=system_prompt_placeholder, lines=3)
        num_prompts = gr.Slider(1, 100, step=1, value=3, label="Number of Data Points to Generate")
        llm_name = gr.Dropdown(
            choices=["gpt4o", "gpt4o-mini", "mistral", "llama3-70b", "anthropic"],
            value="gpt4o",
            label="Select Language Model"
        )
        
        generate_button = gr.Button("Generate Synthetic Data")
        output = gr.Textbox(label="Generated Data", lines=10)
        
        generate_button.click(generate_data_ui, inputs=[sample_prompts, system_prompt, num_prompts, llm_name], outputs=[output])

    return app

if __name__ == "__main__":
    ui = gradio_ui()
    ui.launch()
