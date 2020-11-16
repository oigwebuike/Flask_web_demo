import sqlite3


def show_email(username):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT email FROM users WHERE username = '{username}' ORDER BY pk DESC;""".format(username = username))
    email = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    message = "{username}'s email is {email}.".format(username = username, email = email)

    return message

def check_pwd(username):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE username = '{username}'ORDER BY pk DESC;""".format(username = username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return password

def signup(username, password, email):
    connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE username = '{username}';""".format(username = username))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute("""INSERT INTO users (username, password, email) VALUES('{username}', '{password}', '{email}');""".format(username=username, password=password, email=email))

        connection.commit()
        cursor.close()
        connection.close()


    else:
        return ('User already exists')

    
    return 'You have successfully signed up'



