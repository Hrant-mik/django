# import mysql.connector

# # Connect to MySQL
# conn = mysql.connector.connect(
#     host="localhost",     # Change to your MySQL server host
#     user="root",          # Your MySQL username
#     password="H200313m?",  # Your MySQL password
#     database="school"     # Your database name
# )

# cursor = conn.cursor()

# # Run a simple query (e.g., get all records from a table)
# cursor.execute("SELECT 1")  # Change "users" to your table name

# # Fetch and print results
# for row in cursor.fetchall():
#     print(row)

# # Close connection
# cursor.close()
# conn.close()

import mysql.connector
print("jh")
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
    password="H200313m?",  # Your MySQL password
    database="school",     # Your database name
    connection_timeout=5
    )
    if conn.is_connected():
        print("Connected to MySQL database")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
