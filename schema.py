import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect('teacher_logins.db', check_same_thread=False)
cursor = connection.cursor()
#creating table
cursor.execute(
    """CREATE TABLE teachers(
        teacherID VARCHAR(8),
        password VARCHAR(32),
        fullName VARCHAR(64),
        PRIMARY KEY (teacherID)
    );"""
)

connection.commit()
cursor.close()
connection.close()