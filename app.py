from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/author')
def about_author():
    return render_template('about_author.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

