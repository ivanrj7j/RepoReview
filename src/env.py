from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get('API_KEY')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')