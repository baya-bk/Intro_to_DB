import mysql.connector
from mysql.connector import Error
config = {
    'user': 'root',
    'password': '1234bbq@#',
    'host': 'localhost',
}


def create_database():

    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            print("Database connection successful")

            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


create_database()
