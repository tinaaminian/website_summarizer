from email import message
import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import website_scraper

#Key Validation Check
def validate_api_key() -> None:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("OPENAI_API_KEY is not set")
        return False

    if not api_key.startswith("sk-proj-"):
        print("OPENAI_API_KEY is not valid as it does not start with the expected prefix")
        return False

    if api_key.strip() != api_key:
        print("OPENAI_API_KEY is not valid as it contains leading or trailing whitespace")
        return False

    print("OPENAI_API_KEY is valid")


#prompt builder
def build_prompt(website_content:str) -> list[dict[str, str]]:
    system_prompt = """
        You are a helpful assistant that can analyze the content of a website and
        provide a short summary of the content.
        respond in a markdown format.
    """

    user_prompt = f"""
        Analyze the following website and provide a short summary of the content:
        {website_content}
    
    """
    return [{'role': 'system', 'content': system_prompt}, 
            {'role': 'user', 'content': user_prompt}]

# Summarize website
def website_summarizer(url:str) -> str:
    website_content = website_scraper(url)
    message = build_prompt(website_content)
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",
        input= message
    )
    return response.output_text

def main() -> None:
    validate_api_key()
    url = "https://www.foxnews.com/world/iran-secures-un-role-backing-from-uk-france-canada-australia-us-stands-alone"
    summary = website_summarizer(url)
    print(summary)


if __name__ == "__main__":
    main()