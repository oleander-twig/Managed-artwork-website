PRAGMA foreign_keys=on;
 
DROP TABLE IF EXISTS Picture;

CREATE TABLE Picture (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    img TEXT NOT NULL,
    price INTEGER, 
    descript TEXT NOT NULL
);

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Category;


CREATE TABLE User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_login TEXT NOT NULL,
    user_password TEXT NOT NULL
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Picture(product_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Category (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Picture(product_id)
);
