import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO User (user_login, user_password) VALUES (?, ?)",
            ('admin', '123456789')
            )

connection.commit()
connection.close()
