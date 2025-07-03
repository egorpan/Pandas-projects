import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
html = response.content

books_list = []
instock_list = []
price_list = []

soup = BeautifulSoup(html, 'html.parser')

books = soup.find_all('h3')
for books in books:
    books_list.append(books.text)

instock = soup.find_all('p' , class_='instock availability')
for instock in instock:
    instock_list.append(instock.text.strip())

price = soup.find_all('p', class_='price_color')
for price in price:
    price_list.append(price.text)

df = pd.DataFrame({
    'title' : books_list,
    'instock' : instock_list,
    'price' : price_list
})

print(df)