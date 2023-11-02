from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("MONGO_URL")
api_key = os.getenv("OPENAI_API_KEY")