from email import message
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OPENAI_API_KEY is not set")


elif not api_key.startswith("sk-proj-"):
    print("OPENAI_API_KEY is not valid as it does not start with the expected prefix")

elif api_key.strip() != api_key:
    print("OPENAI_API_KEY is not valid as it contains leading or trailing whitespace")

else:
    print("OPENAI_API_KEY is valid")


client = OpenAI()
message = [{'role': 'user', 'content': 'What is the capital of USA?'}]

response = client.responses.create(
    model="gpt-4o-mini",
    input= message
)
print(response.output_text)

