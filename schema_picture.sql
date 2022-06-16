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

CREATE TABLE Category (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Picture(product_id)
);
