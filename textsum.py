#!pip install requests beautifulsoup4 transformers

import requests
from bs4 import BeautifulSoup
def extract_text(url):
  response=requests.get(url)
  try:
    if response.status_code==200:
      soup=BeautifulSoup(response.text,"html.parser")
      paragraphs=soup.find_all("p")
      article_text=" ".join(p.get_text() for p in paragraphs)
      return article_text
    else:
      return "Failed to retrieve article"
  except Exception as e:
    return f"Error: {str(e)}"

from transformers import pipeline
summarizer=pipeline("summarization",model="facebook/bart-large-cnn",device=0)
def summarize_text(text):
  if len(text)>1024: # Transformer models have input limits
    text=text[:1024]
  summary=summarizer(text,max_length=150,min_length=50,do_sample=False)
  return summary[0]['summary_text']

url = "https://www.bbc.com/news/world-67178877"  # Replace with any article URL
url1="https://www.bbc.com/news/articles/cx2p19l24g2o"
article_text = extract_text(url)
summary = summarize_text(article_text)
print("\nSummary:\n", summary)

