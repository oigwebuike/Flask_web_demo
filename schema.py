import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(20),
        password VARCHAR(50),
        email VARCHAR(50)
    );"""

)

connection.commit()
cursor.close()
connection.close()