import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

class ArticleScraper:
    def __init__(self, website_url):
        self.website_url = website_url

    def retrieve_page(self):
        try:
            response = requests.get(self.website_url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Unable to access {self.website_url}: {e}")
            return None

    def extract_articles(self, html_data):
        try:
            soup = BeautifulSoup(html_data, 'html.parser')
            articles = soup.find_all('article')
            collected_articles = []

            for entry in articles:
                headline = entry.find('h2').get_text(strip=True) if entry.find('h2') else "Untitled"
                content = entry.find('p').get_text(strip=True) if entry.find('p') else "No content"
                collected_articles.append((headline, content))

            return collected_articles

        except Exception as parse_e:
            print(f"Issue parsing the HTML: {parse_e}")
            return []

    def evaluate_sentiment(self, text_data):
        try:
            sentiment_analysis = TextBlob(text_data)
            score = sentiment_analysis.sentiment.polarity
            return score
        except Exception as sentiment_error:
            print(f"Sentiment analysis failed: {sentiment_error}")
            return 0

def execute_scraper():
    news_sites = [
        "https://www.theguardian.com",
        "https://www.cnn.com",
        "https://www.bbc.com/news"
    ]

    for site in news_sites:
        scraper = ArticleScraper(site)
        webpage_content = scraper.retrieve_page()

        if webpage_content:
            articles = scraper.extract_articles(webpage_content)

            for title, description in articles:
                sentiment_score = scraper.evaluate_sentiment(description)
                sentiment_label = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Sentiment: {sentiment_label}\n")

if __name__ == "__main__":
    execute_scraper()
