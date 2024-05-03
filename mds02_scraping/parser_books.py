import csv

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
adapter_rating = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def find_books(cards):
    books = []
    for card in cards:
        info_book = {
            "title": card.find('h3').find('a').get("title").strip(),
            "link": url + card.find('h3').find('a').get("href"),
            "price": card.find('p', class_="price_color").get_text()[1:],
            "thumbnail": url + card.find('img').get("src"),
            "rating": adapter_rating.get(card.find('p', class_="star-rating").get("class")[1])

        }
        books.append(info_book)
    return books


if __name__ == '__main__':
    cards = soup.find_all("article", attrs={"class": "product_pod"})
    result = find_books(cards)
    while True:
        next_link = soup.find("li", class_="next")
        if next_link is None:
            break
        next_url = url + next_link.find("a").get("href")
        if next_url.find("catalogue") == -1:
            next_url = url + "catalogue/" + next_link.find("a").get("href")
        else:
            next_url = url + next_link.find("a").get("href")
        print(next_url)
        page = requests.get(next_url)
        soup = BeautifulSoup(page.content, "html.parser")
        cards = soup.find_all("article", attrs={"class": "product_pod"})
        result = result + find_books(cards)

    print(len(result))
    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link", "price", "thumbnail", "rating"])
        writer.writeheader()
        for book in result:
            writer.writerow(book)
