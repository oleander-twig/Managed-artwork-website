from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_author.sqlite3'

db = SQLAlchemy(app)
class Author(db.Model):
    note_id = db.Column('note_id', db.Integer, primary_key=True)

    title_main = db.Column('title_main', db.String(50))
    text_main = db.Column('text_main', db.String(100))

    logo =  db.Column('logo', db.String(50))

    title_author = db.Column('title_author', db.String(50))
    avatar =  db.Column('avatar', db.String(50))
    text_author =  db.Column('text_author', db.String(100))
    descript =  db.Column('descript', db.String(100))

    fa_link =  db.Column('fa_link', db.String(50))
    inst_link =  db.Column('inst_link', db.String(50))
    wa_link =  db.Column('wa_link', db.String(50))
    tg_link =  db.Column('tg_link', db.String(50))

    passwrd =  db.Column('passwrd', db.String(50))
    lgn =  db.Column('lgn', db.String(50))

    title_gallery =  db.Column('title_gallery', db.String(50))
    text_gallery =  db.Column('text_gallery', db.String(100))

    db.create_all()
    