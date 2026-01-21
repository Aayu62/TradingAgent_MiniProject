import requests
import os

class NewsAnalyst:
    def __init__(self):
        self.api_url = "https://gnews.io/api/v4/search"
        self.api_key = os.getenv("GNEWS_API_KEY")

    def fetch_news(self, query, max_articles=5):
        params = {
            "q": query,
            "lang": "en",
            "max": max_articles,
            "apikey": self.api_key
        }

        try:
            r = requests.get(self.api_url, params=params, timeout=5)
            if r.status_code != 200:
                return []

            data = r.json()
            articles = []

            for a in data.get("articles", []):
                articles.append({
                    "title": a.get("title", ""),
                    "description": a.get("description", "")
                })

            return articles

        except:
            return []
