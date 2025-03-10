# Install required libraries
#!pip install requests beautifulsoup4 transformers

import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def extract_text(url):
    """Extracts text content from a given news article URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        article_text = " ".join(p.get_text() for p in paragraphs)
        
        if not article_text:
            return "No text found in the article."
        
        return article_text.strip()
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching the article: {e}"

def summarize_text(text):
    """Summarizes the extracted text using a transformer model."""
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0)

    if len(text) > 1024:
        text = text[:1024]  # Trim long articles (or implement chunking)

    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# User input for URL
url = input("Enter a news article URL: ").strip()
article_text = extract_text(url)

if "Error" not in article_text:  
    summary = summarize_text(article_text)
    print("\nSummary:\n", summary)
else:
    print("\n", article_text)
