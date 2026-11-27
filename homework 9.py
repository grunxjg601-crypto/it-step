
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]

        print("Назва:", title)
        print("Ціна:", price)
        print("Рейтинг:", rating)
        print("--------------------")

    next_page = soup.find("li", class_="next")

    if next_page:
        url = "https://books.toscrape.com/catalogue/" + next_page.a["href"]
    else:
        url = None
