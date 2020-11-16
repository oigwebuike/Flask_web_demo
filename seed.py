import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute("""INSERT INTO users(
    username, password, email) VALUES('Onyeka', '1234', 'dddooo@gmail.com') """)

cursor.execute("""INSERT INTO users(
    username, password, email) VALUES('Ironman', 'jarvis', 'ironman@gmail.com') """)



connection.commit()
cursor.close()
connection.close()