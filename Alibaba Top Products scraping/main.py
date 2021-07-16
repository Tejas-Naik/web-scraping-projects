from flask import Flask,redirect,url_for,render_template,request
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=paracord&viewtype=&tab=")
audible_webpage = response.text

soup = BeautifulSoup(audible_webpage, "html.parser")
top_products = soup.find_all(name="p", class_="elements-title-normal__content medium")
all_price = soup.find_all(name="p", class_='elements-offer-price-normal medium')

for i in range(len(top_products) - 1):
    print(top_products[i].getText())
    print(all_price[i].getText())
    print()


