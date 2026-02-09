from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
import os


load_dotenv()

model = os.getenv("OPENAI_MODEL", "gpt-5-mini")
 

