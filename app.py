from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main_page():
    title = "Добро пожаловать!"
    text = "Я рисую для души и хочу поделиться своим творчеством с вами! Вот несколько моих работ:"
    description = "Картина номер 1"
    return render_template('main_page.html', context={'title':'Добро пожаловать!', 'text':'Я рисую для души и хочу поделиться своим творчеством с вами! Вот несколько моих работ:', 'description':'Картина номер 1'})

@app.route('/author')
def about_author():
    return render_template('about_author.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/account')
def account():
    return render_template('account.html')
