import os
from dotenv import load_dotenv

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