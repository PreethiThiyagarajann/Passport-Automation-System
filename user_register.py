from mysql.connector import connect, Error
import uuid


def user_register(username, password, email_id, aadhar_card, address, choice):
    uuid_user = uuid.uuid4()
    choice_local = choice
    username_local = username
    password_local = password
    email_id_local = email_id
    aadhar_card_local = aadhar_card
    address_local = address
    status_admin = "pending"
    status_police = "pending"

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

    exists = 1

    for i in result:
        if i[2] == username_local and i[3] == password_local:
            exists = 0
            break

    '''adding record to the table'''
    if exists == 1:
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="root123",
                    database="passport"
            )as connection:
                add_records = f"INSERT INTO users(user_id,choice,username,password,email_id,aadhar_card,address,status_admin,status_police) VALUES('{uuid_user}','{choice_local}','{username_local}','{password_local}','{email_id_local}','{aadhar_card_local}','{address_local}','{status_admin}','{status_police}')"
                with connection.cursor() as cursor:
                    cursor.execute(add_records)
                    connection.commit()
                    return "User added"
        except Error as e:
            print(e)
    else:
        return "This user alredy exists"
