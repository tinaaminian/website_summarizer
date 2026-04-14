import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def website_scraper(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("h1").get_text() if soup.find("h1") else "No title found"
        paragraphs = soup.find_all("p")
        print(len(paragraphs))
        content = "\n".join( p.get_text(strip=True) for p in paragraphs)
        return title + content
    else:
        print(f"Failed to fetch the website: {response.status_code}")




