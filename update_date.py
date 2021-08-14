from mysql.connector import connect, Error

def update_date(user_id,date):
    try:
        with connect(
                host="localhost",
                user="root",
                password="root123",
                database="passport"
        )as connection:
            update_record = f"""UPDATE users
                                SET issue_date='{date}'
                                WHERE user_id='{user_id}'"""
            with connection.cursor() as cursor:
                cursor.execute(update_record)
                connection.commit()
    except Error as e:
        print(e)