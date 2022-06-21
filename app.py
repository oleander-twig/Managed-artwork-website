from re import A
from api import app, queries
from crypt import methods
from flask import render_template
from flask import request
import os



@app.route('/')
def main_page():
    author = queries.get_author(1)
    
    footer = ""

    to_render = '''
    <div class="u-effect-fade u-gallery-item u-gallery-item-{}"><div class="u-back-slide"><img class="u-back-image" src="{}">
</div><div class="u-over-slide u-shading u-over-slide-{}"><h3 class="u-gallery-heading"></h3><p class="u-gallery-text"></p>
</div>
</div>
    '''

    rendered = ''

    for i, picture_data in enumerate(queries.get_starred_pictures()):
        rendered += to_render.format(i, picture_data['img'], i)
        rendered += '\n'

    print(rendered)

    return render_template('main_page.html', context={'title':author['title_main'], 'text':author['text_main'], 'footer':footer}, images_html=rendered)

@app.route('/author')
def about_author():
    return render_template('about_author.html')

@app.route('/gallery')
def gallery():
    to_render = """
    <div class="u-effect-fade u-gallery-item">
              <div class="u-back-slide">
                <img class="u-back-image u-expanded" src="{}">
              </div>
              <div class="u-over-slide u-shading u-over-slide-{}">
                <h3 class="u-gallery-heading"></h3>
                <p class="u-gallery-text"></p>
              </div>
            </div>
    """

    rendered = ''

    for i, picture_data in enumerate(queries.get_all_pictures()):
        rendered += to_render.format(picture_data['img'], i)
        rendered += '\n'

    return render_template('gallery.html', images_html=rendered)

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

@app.route('/redactor', methods=['POST'])
def  redactor_main_page():
    if 'file' in request.files:
        form_data = dict(request.form)
        if 'starred' in form_data.keys():
            form_data['starred'] = True if form_data['starred'] =='on' else False
        else:
            form_data['starred']=False

        print(form_data)

        file = request.files['file']
        filename = file.filename

        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        file.save(path)

        queries.insert_picture(str(path), int(form_data['price']), descript=form_data['descript'],
            starred=form_data['starred'])

        return render_template('redactor.html')

    request_dict = dict(request.form)
    title_main = request_dict['title_main']
    text_main = request_dict['text_main']

    queries.insert(1, title_main=title_main, text_main=text_main)

    return render_template('redactor.html')