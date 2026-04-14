from email import message
import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import website_scraper

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

website_content = website_scraper("https://www.foxnews.com/world/iran-secures-un-role-backing-from-uk-france-canada-australia-us-stands-alone")
system_prompt = """
You are a helpful assistant that can analyze the content of a website and
provide a short summary of the content.
respond in a markdown format.
"""

user_prompt = f"""
Analyze the following website and provide a short summary of the content:
{website_content}
"""

message = [{'role': 'system', 'content': system_prompt}, 
{'role': 'user', 'content': user_prompt}]

response = client.responses.create(
    model="gpt-4o-mini",
    input= message
)
print(response.output_text)

