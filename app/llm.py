from langchain_openai import OpenAI
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = OpenAI(temperature=0.6, openai_api_key=openai_key)

#! Alternatively, can use HuggingFace hub's LLM
# llm = HuggingFaceHub(
#     repo_id='google/flan-t5-large', model_kwargs={"temperature": 0.7, "max_length": 256}
# )
