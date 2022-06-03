from flask import Flask, render_template


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
