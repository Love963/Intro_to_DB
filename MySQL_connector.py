import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="tamirat",
    password="fiker963",
    database="alx_book_store"  # Use your database name
)

cursor = db.cursor()

# Run your query
cursor.execute("SELECT * FROM users")

# Print results
for row in cursor.fetchall():
    print(row)

db.close()