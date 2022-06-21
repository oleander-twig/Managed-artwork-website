from api import db


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

db.create_all()

author = Author()
author.title_main = "ASD"

db.session.add(author)
db.session.commit()
