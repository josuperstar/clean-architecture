import sqlite3

connection = sqlite3.connect('database.db')


with open('../../../adapters/gateways/sql_lite/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO shots (title, description, cost, budget) VALUES (?, ?, ?, ?)",
            ('First Shot', 'Description for the first shot', 100, 200)
            )

cur.execute("INSERT INTO shots (title, description, cost, budget) VALUES (?, ?, ?, ?)",
            ('Second Shot', 'Description for the second shot', 200,100)
            )

connection.commit()
connection.close()
