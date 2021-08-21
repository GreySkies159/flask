import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
        )VALUES(
            'root',
            'root',
            'root'
        );"""

)

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
        )VALUES(
            'name',
            'pass',
            'color'
        );"""

)

connection.commit()
cursor.close()
connection.close()
