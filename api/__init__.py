from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_author.sqlite3'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config ['UPLOAD_FOLDER'] = './static/images'

author_db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_main.sqlite3'

main_db = SQLAlchemy(app)
