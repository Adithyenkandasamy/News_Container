import os
import requests
from services.summary_ai import summarize_article
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_top_news(country="in", category="general", count=5):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "category": category,
        "apiKey": NEWS_API_KEY,
        "pageSize": count
    }

    response = requests.get(url, params=params)
    
    print("API STATUS CODE:", response.status_code)
    print("API RAW RESPONSE:", response.json())

    if response.status_code != 200:
        return [{"error": "Failed to fetch news", "details": response.text}]
    
    articles = response.json().get("articles", [])

    result = []
    for article in articles:
        content = article.get("description") or article.get("content") or ""
        summary = summarize_article(content)

        result.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "url": article["url"],
            "summary": summary
        })

    return result
