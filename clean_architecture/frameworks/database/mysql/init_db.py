
from clean_architecture.frameworks.database.mysql.mysql_adapter import *

connection = get_db_connection()

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS element (
    id int(5) NOT NULL AUTO_INCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name varchar(50) DEFAULT NULL,
    content varchar(50) DEFAULT NULL,
    PRIMARY KEY(id)
);
""")

cur = connection.cursor()
print('adding test data')
cur.execute("INSERT INTO element (name, content) VALUES (%s, %s)",
            ('First Shot', 'Description for the first shot')
            )

cur.execute("INSERT INTO element (name, content) VALUES (%s, %s)",
            ('Second Shot', 'Description for the second shot')
            )

connection.commit()
connection.close()
