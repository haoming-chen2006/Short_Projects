from bs4 import BeautifulSoup
import requests
import csv

with open('books.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title','Rating',"Price"])
    for i in range(1,50):
        url = "https://books.toscrape.com/catalogue/category/books_1/page-"+str(i)+".html"
        target_book = requests.get('https://books.toscrape.com/catalogue/category/books_1/page-1.html')
        soup = BeautifulSoup(target_book.text, "html.parser")
        ol = soup.find('ol')
        articles = ol.find_all('article', class_="product_pod")
        prices = ol.find_all('p', class_="price_color")
        for article in articles:
            img = article.find('img')
            title = img.attrs['alt']
            star = article.find('p')
            rate = star.attrs['class'][1]
            price = article.find("p",class_='price_color').text
            price = float(price[2:])
            write = [title,rate,price]
            writer.writerow(write)









