from mysql.connector import connect, Error


def check_status_func(username, password):
    try:
        with connect(
                host="localhost",
                user="root",
                password="root123",
                database="passport"
        )as connection:
            view_records = "SELECT * FROM users"
            with connection.cursor() as cursor:
                cursor.execute(view_records)
                result = cursor.fetchall()
    except Error as e:
        print(e)
    flag = 1
    counter = 0
    username_local = username
    password_local = password
    for i in result:
        if i[2] == username_local and i[3] == password_local:
            flag = 0
            break
        counter += 1
    return i[7], i[8],i[9], flag
