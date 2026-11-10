import os
from dotenv import load_dotenv

def load_keys():
    load_dotenv()

    API_KEY_1 = os.getenv("API_KEY_1")
    API_KEY_2 = os.getenv("API_KEY_2")
    API_KEY_3 = os.getenv("API_KEY_3")

    return API_KEY_1, API_KEY_2, API_KEY_3