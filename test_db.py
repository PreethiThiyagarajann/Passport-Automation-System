from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="root123"
    ) as connection:
        create_db_query = "CREATE DATABASE passport"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

