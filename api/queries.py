from .models import Author
from api import db


def get_author(note_id):
    author = Author.query.get(note_id) #вернет объект класса Author
    return author.to_dict()

def insert(note_id, title_main="", text_main=""):
    author = Author.query.get(note_id) #вернет объект класса Author

    if title_main:
        author.title_main = title_main
    if text_main:
        author.text_main = text_main

    db.session.add(author)
    db.session.commit()
