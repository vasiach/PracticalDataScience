import re
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.gutenberg.org/ebooks/search/?query=Charles%09Dickens")
html = r.content
soup = BeautifulSoup(html, 'html.parser')
review_results = soup.find_all("li", {"class":{"booklink"}})

titles = set()
for result in review_results:
    titles.update( result.find_all(class_="title"))

for i, title in enumerate(titles):
    print(i, title)

