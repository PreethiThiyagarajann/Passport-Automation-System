from mysql.connector import connect, Error


def police_verify_func(user_id):
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
    if flag == 1:
        return "User not found", flag
    else:
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="root123",
                    database="passport"
            )as connection:
                update_record = f"""UPDATE users
                                SET status_police="verified"
                                WHERE user_id='{result[counter][0]}'"""
                with connection.cursor() as cursor:
                    cursor.execute(update_record)
                    connection.commit()
                    return "Details Verified", flag
        except Error as e:
            print(e)
        else:
            return "verification has been denied", flag
