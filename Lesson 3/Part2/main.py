from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/Deep_learning"
openPage = urlopen(url)

html = openPage.read().decode("utf-8")

titleStart = html.find("<title>") + len("<title>")
titleEnd = html.find("</title>")

title = html[titleStart:titleEnd]

print("Page title: ", title)

soup = BeautifulSoup(html, "html.parser")

links = []
aTags = soup.find_all("a")
for tag in aTags:
    links.append(tag.get("href"))

for x in links:
    print(x)