import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO shots (title, description) VALUES (?, ?)",
            ('First Shot', 'Description for the first shot')
            )

cur.execute("INSERT INTO shots (title, description) VALUES (?, ?)",
            ('Second Shot', 'Description for the second shot')
            )

connection.commit()
connection.close()
