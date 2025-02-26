import os
import uuid
from bson import Binary
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_ollama import ChatOllama
from app.utils.llm.embeddings import calculate_embedding_similarities, get_embeddings
from app.models.prompt import Prompt


THRESHOLD = 0.8

class SyntheticPrompts(BaseModel):
    prompts: list[str] = Field(description="List of sample data entries")


class SyntheticDataGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")  # Default model

    def update_llm(self, llm_name):
        # Dynamically switch LLMs based on the llm_name
        if llm_name == "gpt4o":
            self.llm = ChatOpenAI(model="gpt-4o")
        elif llm_name == "gpt4o-mini":
            self.llm = ChatOpenAI(model="gpt-4o-mini")
        elif llm_name == "mistral":
            self.llm = ChatMistralAI(model="mistral-7b")
        elif llm_name == "llama3-70b":
            self.llm = ChatOllama(model="llama3-70b")
        elif llm_name == "anthropic":
            self.llm = ChatOllama(model="anthropic-claude")
        else:
            raise ValueError(f"Unknown LLM name: {llm_name}")

    def generate_batch(self, sample_prompts, system_prompt, num_prompts):
        # Prepare the input prompt
        # Add batching logic here
        # BATCH_SIZE and NUM_RUNS
        # prompt = ChatPromptTemplate.from_template(f"{system_prompt} {samples}")

        # Generate structured output using Pydantic model
        structured_llm = self.llm.with_structured_output(SyntheticPrompts)
        prompt = f"Generate {num_prompts} prompts. " + system_prompt + "\n" + sample_prompts
        synthetic_prompts = structured_llm.invoke(prompt)
        
        synthetic_embeddings = get_embeddings(synthetic_prompts.prompts)
        db_embeddings = Prompt.get_all_embeddings()
        # Handle the case when there are no entries in the db
        if db_embeddings.size == 0:
            unique_indices = list(range(len(synthetic_prompts.prompts)))
        
        else:
            unique_indices = calculate_embedding_similarities(
                synthetic_embeddings, db_embeddings, THRESHOLD
            )

        for i in unique_indices:
            prompt = synthetic_prompts.prompts[i]
            Prompt.create_prompt(
                {
                    "content": prompt,
                    "embeddings": synthetic_embeddings[i].tolist(),
                    "tags": ["synthetic"],
                    "project": "67a9b4465a4ef2bdd95cc95c"
                }
            )

        return [synthetic_prompts.prompts[i] for i in unique_indices]


if __name__ == "__main__":
    generator = SyntheticDataGenerator()
    samples = """
Phone start rotating slowly & followed by a more dramatic rotation and finally rotation ends slowly after completing 2 rounds at the origin. Duration is 7 seconds.
Phone travels to the side while rotating. duration 7 seconds
Phone oscillates just above the podium maintaining the centre position and rotates from left to right. Animation continues for 7 seconds
Phone tilts back and forth while positioned at the origin. duration 7 seconds
"""
    system_prompt = "You are a marketing person. You are tasked to create a marketing campain to increase the sales of mobile phones. You have a tool at your disposal using which phone advertisement videos can be created using simple text prompts. The text input to this tool should describe only the animation of the phone and no other details. Using the below prompts as few examples, please generate more prompts which I can use with my tool. Make sure the created twxt prompt is well formatted."
    generated_data = generator.generate_batch(samples, system_prompt, 10)
    print(type(generated_data))
    for sample in generated_data.samples:
        print(sample)
