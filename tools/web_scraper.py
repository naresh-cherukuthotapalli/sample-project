import requests
from bs4 import BeautifulSoup

def scrape_website(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        text = text.replace('\xa0', ' ').strip()
        return { "content": text[:2000] }  # Limit to first 2000 characters
    except Exception as e:
        return { "error": str(e) }
