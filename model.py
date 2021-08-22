import sqlite3

def full_name(ID):
    connection = sqlite3.connect('teacher_logins.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT fullName FROM teachers WHERE teacherID='{ID}' ORDER BY teacherID DESC;""".format(ID = ID))
    name = cursor.fetchone()[0]
    print("gotten full", name)

    connection.commit()
    cursor.close()
    connection.close()
    message = '{name}.'.format(name=name)
    return message


def check_pw(ID, given_password):
    connection = sqlite3.connect('teacher_logins.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM teachers WHERE teacherID ='{ID}' ORDER BY teacherID DESC;""".format(ID = ID))
    password  = cursor.fetchone()[0]
    print("gotten password in model from db- ", password)

    if password == None:
        return "ID not found"

    connection.commit()
    cursor.close()
    connection.close()

    if given_password==password:
        return "True"
    else:
        return "False"


def signup(ID, password, full_name):
    connection = sqlite3.connect('teacher_logins.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM teachers WHERE teacherID = '{ID}';""".format(ID = ID))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute("""INSERT INTO teachers(teacherID, password, fullName)VALUES('{ID}', '{password}', '{full_name}');""".format(ID = ID, password=password, full_name=full_name))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return ('Teacher already exists')

    return 'You have successfully signed up!'

#check if this is correct
def check_users():
    connection = sqlite3.connect('teacher_logins.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT teacherID FROM teachers ORDER BY teacherID DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return users