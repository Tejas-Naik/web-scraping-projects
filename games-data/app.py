from flask import Flask,redirect,url_for,render_template,request
from main import game_names, game_prices

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', game_names=game_names, game_prices=game_prices)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)