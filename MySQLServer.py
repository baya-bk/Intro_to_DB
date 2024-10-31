import mysql.connector
from mysql.connector import Error

config = {
    'user': 'root',
    'password': '1234bbq@#',
    'host': 'localhost',
    'database': 'alx_book_store'
}


def create_books_table():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("atabase 'alx_book_store' created successfully!")

            cursor = connection.cursor()

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


create_books_table()
