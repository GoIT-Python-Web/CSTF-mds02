import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


# link = soup.find("a")
# print(link)

# links = soup.find_all("a")
# print(links)

# content = link.get_text()
# print(content)
#
# content = link.text
# print(content)
#
# attr = link.get("href")
# print(attr)

# cards = soup.find_all("article", class_="product_pod")
cards = soup.find_all("article", attrs={"class": "product_pod"})
card = cards[0]

title = card.find('h3').find('a').get("title")
print(title)
link = url + card.find('h3').find('a').get("href")
print(link)
price = card.find('p', class_="price_color").get_text()[1:]
print(price)
thumbnail = url + card.find('img').get("src")
print(thumbnail)
adapter_rating = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
rating = adapter_rating.get(card.find('p', class_="star-rating").get("class")[1])
print(rating)