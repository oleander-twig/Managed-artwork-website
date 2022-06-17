import sqlite3

connection = sqlite3.connect('database_author.db')


#create a table for author data
with open('schema_author.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Author (lgn, passwrd) VALUES (?, ?)",
            ('admin', '123456789')
            )

connection.commit()
connection.close()


connection = sqlite3.connect('database_picture.db')

#create a table for picture data
with open('schema_picture.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

connection.commit()
connection.close()
