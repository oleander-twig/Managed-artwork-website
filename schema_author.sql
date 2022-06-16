DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Picture;
DROP TABLE IF EXISTS Author;


CREATE TABLE Author (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title_main TEXT ,
    text_main TEXT ,
    logo TEXT ,
    title_author TEXT ,
    avatar TEXT ,
    text_author TEXT ,
    descript TEXT ,
    fa_link TEXT ,
    inst_link TEXT ,
    wa_link TEXT ,
    tg_link TEXT , 
    passwrd TEXT ,
    lgn TEXT ,
    title_gallery TEXT ,
    text_gallery TEXT 
);