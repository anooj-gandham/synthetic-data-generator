import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    DEBUG = True
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/synthetic_data_db")
