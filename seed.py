import sqlite3

connection = sqlite3.connect('teacher_logins.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO teachers(
        teacherID,
        password,
        fullName
        )VALUES(
            'root',
            'root',
            'root'
        );"""

)

cursor.execute(
    """INSERT INTO teachers(
        teacherID,
        password,
        fullName
        )VALUES(
            '00000001',
            'password',
            'Eglė Kasperavičiūtė'
        );"""

)

connection.commit()
cursor.close()
connection.close()
