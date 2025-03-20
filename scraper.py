import requests
from bs4 import BeautifulSoup
import re

def scrape_emails(url):
    """Scrapes emails from a given website URL."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  # Mimics a real browser
        response = requests.get(url, headers=headers, timeout=10)  # Fetch the webpage
        
        if response.status_code == 200:  # Successful response
            soup = BeautifulSoup(response.text, "html.parser")  
            emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", soup.text)  # Extract emails
            return list(set(emails))  # Remove duplicates
        else:
            return f"Error: Received status code {response.status_code}"
    
    except Exception as e:
        return f"Request failed: {e}"

# Example usage (For testing, remove when integrating with Streamlit)
if __name__ == "__main__":
    test_url = "https://example.com"
    print(scrape_emails(test_url))
