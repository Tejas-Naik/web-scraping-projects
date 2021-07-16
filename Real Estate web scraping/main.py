from flask import Flask,redirect,url_for,render_template,request
from bs4 import BeautifulSoup
import requests

real_estate_website = requests.get("https://www.trulia.com/houses-for-sale-near-me/").text
soup = BeautifulSoup(real_estate_website, "html.parser")

all_price = soup.find_all(name="div", class_="Text__TextBase-sc-1cait9d-0-div Text__TextContainerBase-sc-1cait9d-1 keMYfJ")
all_images = soup.find_all(name="img", class_="Image__ImageContainer-sc-1motiir-0 hPjFaC")

for image in all_images:
    print(image.get("src"))

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', images=all_images, prices=all_price)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
