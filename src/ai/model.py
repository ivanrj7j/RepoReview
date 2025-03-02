from google import genai
from google.genai import types
from .. import env

client = genai.Client(api_key=env.GEMINI_API_KEY)
model = "gemini-2.0-flash"