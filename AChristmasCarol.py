import re
from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.gutenberg.org/cache/epub/30368/pg30368.txt")
text = r.content
soup = BeautifulSoup(text, "lxml")
carol = soup.find('body').get_text()
#
sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', carol)
count = 1
for sent in sentences:
    if 'THE END.' in sent:
        break
    if 'Scrooge' in sent:
        pretty_sentence = re.sub('(\[[^]]*])', ' ', sent)
        pretty_sentence = re.sub('\s+', ' ', pretty_sentence)
        print(count, pretty_sentence)
        count += 1

