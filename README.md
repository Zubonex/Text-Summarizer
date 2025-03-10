# Text-Summarizer
# 📰 Text Summarization Tool  

This project extracts text from news articles and summarizes them using **Facebook's BART model**. It leverages **web scraping (BeautifulSoup)** and **NLP (Hugging Face Transformers)** to generate concise summaries.

## 🚀 Features  
- Extracts text from any news article URL  
- Uses **BART Large CNN** for high-quality text summarization  
- Automatically trims long articles to fit model limits  
- Provides easy-to-use Python script  

---

## 🛠 Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
## Install Dependencies
pip install requests beautifulsoup4 transformers torch
## Run the script
python summarizer.py
##Technologies Used
Python
Requests (for fetching article content)
BeautifulSoup4 (for extracting text)
Hugging Face Transformers (for summarization)
Facebook BART Large CNN model
📜 License
This project is licensed under the MIT License.
