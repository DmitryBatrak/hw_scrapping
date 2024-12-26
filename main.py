import bs4
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get("https://habr.com/ru/articles/")
soup = bs4.BeautifulSoup(response.text, "lxml")
articles = soup.select("article.tm-articles-list__item")

for article in articles:
    if any(keyword in article.text.lower() for keyword in KEYWORDS):
        art_date = article.select_one("time")
        art_name = article.select_one("a.tm-title__link")
        print(art_date["title"][:10], art_name.text, f"https://habr.com{art_name["href"]}")


