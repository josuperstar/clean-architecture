connection = get_db_connection()

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS element (
    id int(5) NOT NULL AUTO_INCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name varchar(50) DEFAULT NULL,
    content varchar(50) DEFAULT NULL,
    expense_to_date int(5) DEFAULT NULL,
    shot_bid int(5) DEFAULT NULL,
    PRIMARY KEY(id)
);
""")

cur = connection.cursor()
print('adding test data')
cur.execute("INSERT INTO element (name, content, expense_to_date, shot_bid) VALUES (%s, %s, %s, %s)",
            ('First Shot', 'Description for the first shot', 200, 100)
            )

cur.execute("INSERT INTO element (name, content, expense_to_date, shot_bid) VALUES (%s, %s, %s, %s)",
            ('Second_Shot', 'Description for the second shot', 100, 200)
            )

connection.commit()
connection.close()
