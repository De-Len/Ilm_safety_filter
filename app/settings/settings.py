import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    EXTERNAL_LLM_URL = os.getenv("EXTERNAL_LLM_URL")
    EXTERNAL_LLM_API_KEY = os.getenv("EXTERNAL_LLM_API_KEY")
    EXTERNAL_LLM_MODEL_NAME = os.getenv("EXTERNAL_LLM_MODEL_NAME")
