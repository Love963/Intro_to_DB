# import mysql.connector
# from mysql.connector import Error

# def create_database():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='pythonuser',
#             password='Tamirat963'
#         )

#         if connection.is_connected():
#             cursor = connection.cursor()
#             cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
#             print("Database 'alx_book_store' created successfully!")

#     except Error as e:
#         print("Error:", e)

#     finally:
#         if 'connection' in locals() and connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed.")

# create_database()


# import mysql.connector
# from mysql.connector import Error

# def create_database_and_tables():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='pythonuser',
#             password='Tamirat963'
#         )

#         if connection.is_connected():
#             cursor = connection.cursor()

#             # Create database
#             cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
#             cursor.execute("USE alx_book_store")

#             # Create tables
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS Authors (
#                     author_id INT PRIMARY KEY,
#                     author_name VARCHAR(215)
#                 )
#             """)

#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS Books (
#                     book_id INT PRIMARY KEY,
#                     title VARCHAR(130),
#                     author_id INT,
#                     price FLOAT,
#                     publication_date DATE,
#                     FOREIGN KEY (author_id) REFERENCES Authors(author_id)
#                 )
#             """)

#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS Customers (
#                     customer_id INT PRIMARY KEY,
#                     customer_name VARCHAR(215),
#                     email VARCHAR(215),
#                     address VARCHAR(255)
#                 )
#             """)

#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS Orders (
#                     order_id INT PRIMARY KEY,
#                     customer_id INT,
#                     order_date DATE,
#                     FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
#                 )
#             """)

#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS Order_Details (
#                     orderdetailid INT PRIMARY KEY,
#                     order_id INT,
#                     book_id INT,
#                     quantity FLOAT,
#                     FOREIGN KEY (order_id) REFERENCES Orders(order_id),
#                     FOREIGN KEY (book_id) REFERENCES Books(book_id)
#                 )
#             """)

#             print("Database and tables created successfully!")

#     except Error as e:
#         print(" Error:", e)

#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("🔌 MySQL connection closed.")

# create_database_and_tables()



import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="tamirat",
    password="fiker963",
    database="alx_book_store"
)

cursor = conn.cursor()

# Run a query
cursor.execute("SELECT * FROM Customers")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()