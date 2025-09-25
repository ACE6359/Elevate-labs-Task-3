import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
import os
import csv
import sys

# ----------------- CONFIG -----------------
# Option 1: Hardcode a URL
# URLS = ["https://www.bbc.com/news"]

# Option 2: Take URLs from command line arguments
# Hardcode multiple URLs
URLS = [
    "https://www.bbc.com/news",
    "https://edition.cnn.com",
    "https://www.aljazeera.com"
]


# ----------------- SCRAPER -----------------
def scrape_headlines(url):
    """Fetch headlines from a news website."""
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text and text not in headlines:  # remove duplicates
            headlines.append(text)
    return headlines

# ----------------- SAVE FUNCTION -----------------
def save_headlines(site_name, headlines):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    folder = "output"
    os.makedirs(folder, exist_ok=True)
    base_name = os.path.join(folder, f"{site_name}_headlines_{timestamp}")

    # TXT
    with open(base_name + ".txt", "w", encoding="utf-8") as f:
        for i, hl in enumerate(headlines, start=1):
            f.write(f"{i}. {hl}\n")

    # CSV
    with open(base_name + ".csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["S.No", "Headline"])
        for i, hl in enumerate(headlines, start=1):
            writer.writerow([i, hl])

    print(f"✅ {len(headlines)} headlines saved to {base_name}.txt and {base_name}.csv")

# ----------------- MAIN -----------------
for url in URLS:
    print(f"\n🔍 Scraping: {url}")
    site_name = urlparse(url).netloc.replace(".", "_")
    headlines = scrape_headlines(url)
    if headlines:
        save_headlines(site_name, headlines)
    else:
        print("⚠️ No headlines found.")
