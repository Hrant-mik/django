import pyodbc

# Define the connection string
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=my_school;'
    'UID=root;'
    'PWD=H200313m?'
)

# Establish the connection
conn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = conn.cursor()

# Execute a simple SQL query
cursor.execute("SELECT 1")

# Fetch and display the results
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()