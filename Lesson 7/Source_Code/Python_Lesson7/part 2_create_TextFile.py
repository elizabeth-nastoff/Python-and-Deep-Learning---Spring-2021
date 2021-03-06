import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Google")
soup = BeautifulSoup(r.text, 'html.parser')

f = open("input.txt", "w", encoding='utf-8')

f.write(str(soup))

f.close()