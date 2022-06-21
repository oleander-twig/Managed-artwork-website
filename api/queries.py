from ast import main
from nis import cat
from .models import Author, Category, Picture
from api import author_db, main_db


def get_author(note_id):
    author = Author.query.get(note_id) #вернет объект класса Author
    return author.to_dict()

def insert(note_id, title_main="", text_main=""):
    author = Author.query.get(note_id) #вернет объект класса Author

    if title_main:
        author.title_main = title_main
    if text_main:
        author.text_main = text_main

    author_db.session.add(author)
    author_db.session.commit()

def get_picture(id):
    try:
        picture = Picture.query.get(id)
        payload = picture.to_dict()
    except:
        payload = Picture().to_dict()
    
    return payload

def insert_picture(img='', price=0, descript='Just an image', starred=False): # need to add parameters here
    picture = Picture(img=img, price=price, descript=descript, starred=starred)

    main_db.session.add(picture)
    main_db.session.commit()

    return picture.to_dict()

def get_all_pictures():
    pictures = Picture.query.all()
    
    return [obj.to_dict() for obj in pictures]

def get_starred_pictures():
    starred = Picture.query.filter_by(starred=True).all()

    print(starred)
    
    return [obj.to_dict() for obj in starred]

def get_all_pictures_by_category(category_id): # returns list of picture data
    picture_ids = Category.query.filter_by(category_id=category_id).all()
    return [obj.to_dict() for obj in picture_ids]

def set_picture_category(product_id, category_id): # add row to Category table

    try:
        category = Category(category_id=category_id, product_id=product_id)
        
        main_db.session.add(category)
        main_db.session.commit()
        
        payload = category.to_dict()
    except:
         payload = Category().to_dict()
    
    return payload
