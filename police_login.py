from mysql.connector import connect, Error

def police_login_func(username,password):
    try:
        with connect(
            host="localhost",
            user="root",
            password="root123",
            database="passport"
        )as connection:
            view_records = "SELECT * FROM police"
            with connection.cursor() as cursor:
                cursor.execute(view_records)
                result = cursor.fetchall()
    except Error as e:
        print(e)
    access = 1
    flag = 1
    counter = 0
    username_local = username
    for i in result:
        if i[1] == username_local:
            flag = 0
            break
        counter += 1
    if flag == 0:
        password_local = password
        if password_local == result[counter][2]:
            access = 0
            return "access granted to " + result[counter][0] + " " + result[counter][1], access
        else:
            return "access denied", access
    else:
        return "User not found as a police officer", access

