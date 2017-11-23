import requests
from bs4 import BeautifulSoup


def find_titles(url):
    titles=[]
    while True:
        try:
            r = requests.get("https://www.gutenberg.org" + url)

        except requests.exceptions.RequestException as rex:
            print("Unable to get {article_url} reason {rex}")
        else:
            html = r.content
            soup = BeautifulSoup(html, 'html.parser')
            review_results = soup.find_all("li", {"class": {"booklink"}})
            for result in review_results:
                if result.find("span", class_="subtitle") is not None:
                    author = result.find('span', class_="subtitle").get_text()
                    if "Charles Dickens" in author:
                        for x in result.find_all(class_="title"):
                            titles.append(x.get_text())

            statuslinks = soup.find_all("li", {"class": {"statusline"}})
            for link in statuslinks:
                next_page = link.find_all("a", {"title": "Go to the next page of results."}, href=True)
            if not next_page:
                break
            else:
                for i in next_page:
                    url = i["href"]
    return titles


url_link = "/ebooks/search/?&query=charles+dickens"
books = set(find_titles(url_link))
for i, title in enumerate(books):
    print(i, title)
