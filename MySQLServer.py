import mysql.connector
import mysql.connector Error

try:
    # Connect to MySQL Server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='PhindiKunene85$'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close the connection safely
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
