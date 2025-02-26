import requests

# API Base URL
BASE_URL = "http://127.0.0.1:5001/api"  # Change if needed

def get_all_prompts():
    """Fetch all prompts from the API."""
    response = requests.get(f"{BASE_URL}/prompts")
    
    if response.status_code == 200:
        return response.json()  # Return list of prompts
    else:
        print("Failed to fetch prompts:", response.text)
        return []

def delete_prompt(prompt_id):
    """Delete a specific prompt by ID."""
    response = requests.delete(f"{BASE_URL}/prompts/{prompt_id}")
    
    if response.status_code == 204:
        print(f"Deleted prompt ID: {prompt_id}")
    else:
        print(f"Failed to delete prompt {prompt_id}: {response.text}")

def delete_all_prompts():
    """Fetch and delete all prompts."""
    prompts = get_all_prompts()
    
    if not prompts:
        print("No prompts found to delete.")
        return
    
    for prompt in prompts:
        prompt_id = prompt.get("id")  # Extract prompt ID
        if prompt_id:
            delete_prompt(prompt_id)

if __name__ == "__main__":
    delete_all_prompts()
