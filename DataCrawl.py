import re
import requests
from bs4 import BeautifulSoup

def get_internal_links(soup, include_url):
    internal_links = set()
    # Finds all links that may begin with a "/"
    # An internal link either starts with a "/" or contains the site name
    for link in soup.find_all("a",
                             href=re.compile("^(/|.*" + include_url + ")")):
        if link.attrs['href'] is not None:
            internal_links.add(link.attrs['href'])
    return internal_links


r = requests.get("https://www.gutenberg.org/ebooks/search/?query=Charles%09Dickens")
html = r.content
soup = BeautifulSoup(html, 'html.parser')




review_results = soup.find_all("li", {"class": {"booklink"}})


titles = set()
for result in review_results:

    author = result.find('span', class_="subtitle").get_text()
    print (author)
    titles.update(result.find_all(class_="title"))

for i, title in enumerate(titles):
    print(i, title)

