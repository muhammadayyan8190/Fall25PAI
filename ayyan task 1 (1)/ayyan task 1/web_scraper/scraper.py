import re
import requests
from bs4 import BeautifulSoup

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}")


def scrape_emails_from_url(url: str) -> list[str]:
    """Fetch the page at `url` and return a list of unique email addresses found."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception:
        return []

    text = response.text
    found = set(EMAIL_REGEX.findall(text))
    return sorted(found)
