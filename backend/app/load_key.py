import os
from dotenv import load_dotenv

def load_key():
    load_dotenv()

    API_KEY = os.getenv("GROQ_API_KEY")

    return API_KEY