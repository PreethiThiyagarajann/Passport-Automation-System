from mysql.connector import connect, Error


def find_user(user_id):
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
    user_id_local = user_id
    counter = 0
    flag = 1
    for i in result:
        if i[0] == user_id_local:
            flag = 0
            break
        counter += 1
    return i, flag
