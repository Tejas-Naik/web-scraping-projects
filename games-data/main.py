from bs4 import BeautifulSoup
import bs4
import requests

game_website = requests.get("https://www.vulture.com/article/best-video-games-2021.html").text

soup = BeautifulSoup(game_website, "html.parser")

print(soup.title)

game_names = []
game_prices = []

games = soup.find_all(name="h2", class_='clay-subheader')
for game in games:
    game_names.append(game.getText())

prices = soup.find_all(name='span', class_='product-buy-price')
for price in prices:
    game_prices.append(price.getText().split()[0])
