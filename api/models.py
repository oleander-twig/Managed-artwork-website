from itertools import product
from api import author_db
from api import main_db


class Author(author_db.Model):
    note_id = author_db.Column('note_id', author_db.Integer, primary_key=True)

    title_main = author_db.Column('title_main', author_db.String(50))
    text_main = author_db.Column('text_main', author_db.String(100))

    logo =  author_db.Column('logo', author_db.String(50))

    title_author = author_db.Column('title_author', author_db.String(50))
    avatar =  author_db.Column('avatar', author_db.String(50))
    text_author =  author_db.Column('text_author', author_db.String(100))
    descript =  author_db.Column('descript', author_db.String(100))

    fa_link =  author_db.Column('fa_link', author_db.String(50))
    inst_link =  author_db.Column('inst_link', author_db.String(50))
    wa_link =  author_db.Column('wa_link', author_db.String(50))
    tg_link =  author_db.Column('tg_link', author_db.String(50))

    passwrd =  author_db.Column('passwrd', author_db.String(50))
    lgn =  author_db.Column('lgn', author_db.String(50))

    title_gallery =  author_db.Column('title_gallery', author_db.String(50))
    text_gallery =  author_db.Column('text_gallery', author_db.String(100))

    def to_dict(self):
        dict = {
            'note_id':self.note_id,
            'title_main':self.title_main,
            'text_main':self.text_main,
            'logo':self.logo,
            'title_author':self.title_author,
            'avatar':self.avatar,
            'text_author':self.text_author,
            'descript':self.descript,
            'fa_link':self.fa_link,
            'inst_link':self.inst_link,
            'wa_link':self.wa_link,
            'tg_link':self.tg_link,
            'passwrd':self.passwrd,
            'lgn':self.lgn,
            'title_gallery':self.title_gallery,
            'text_gallery':self.text_gallery
        }
        
        return dict

class Picture(main_db.Model):
    product_id = main_db.Column('product_id', main_db.Integer, primary_key=True)
    img = main_db.Column('img', main_db.String(50))
    price = main_db.Column('price', main_db.Integer)
    descript = main_db.Column('descript', main_db.String(100))
    starred = main_db.Column('starred', main_db.Boolean)

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'img': self.img,
            'price': self.price,
            'descript': self.descript,
            'starred': self.starred
        }


class Category(main_db.Model):
    record_id = main_db.Column('record_id', main_db.Integer, primary_key=True)
    category_id = main_db.Column('category_id', main_db.Integer)
    product_id = main_db.Column('product_id', main_db.Integer, main_db.ForeignKey('picture.product_id'))
    
    def to_dict(self):
        return {
            'record_id': self.record_id,
            'category_id': self.category_id,
            'product_id': self.product_id
        }

author_db.create_all()

author = Author()

author_db.session.add(author)
author_db.session.commit()

main_db.create_all()
