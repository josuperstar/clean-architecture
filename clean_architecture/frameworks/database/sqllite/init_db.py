import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO shots (title, description, cost, budget) VALUES (?, ?, ?, ?)",
            ('First Shot', 'Description for the first shot', 100, 200)
            )

cur.execute("INSERT INTO shots (title, description, cost, budget) VALUES (?, ?, ?, ?)",
            ('Second Shot', 'Description for the second shot', 200, 100)
            )

cur.execute("INSERT INTO assets (name, description, cost) VALUES (?, ?, ?)",
            ('Primary Asset', 'Description for the second shot', 50)
            )

cur.execute("INSERT INTO shot_asset_relationships (shot_reference, asset_reference) VALUES (?, ?)",
            (1,1)
            )

cur.execute("INSERT INTO shot_asset_relationships (shot_reference, asset_reference) VALUES (?, ?)",
            (2,1)
            )

connection.commit()
connection.close()
