from crypt import methods
from flask import Flask, render_template
from flask import request


app = Flask(__name__, template_folder='./templates')

@app.route('/')
def main_page():
    title = "Добро пожаловать!"
    text = "Я рисую для души и хочу поделиться своим творчеством с вами! Вот несколько моих работ:"
    footer = "Сайт Евгения Северенкова"
    return render_template('main_page.html', context={'title':title, 'text':text, 'footer':footer})

@app.route('/author')
def about_author():
    return render_template('about_author.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/edit_site')
def edit_site():
    return render_template('edit_site.html')

@app.route('/edit_site', methods=['POST'])
def edit_site_post():
    login = request.args.get('login')
    password = request.args.get('password')
    #more todo
    return render_template('edit_site.html')

@app.route('/redactor')
def redactor():
    return render_template('redactor.html')
