import psycopg2
import sys

print("Script starting...")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

# Try a very basic connection test
try:
    print("Attempting database connection...")
    conn = psycopg2.connect(
        host='mlb-the-show-db.clw2io0soo2o.us-east-2.rds.amazonaws.com',
        database='mlb-the-show-db',
        user='skeebo',
        password='ChicagoBearsSP24!',
        port='5432'
    )
    print("Connection successful!")
    
    # Test creating a cursor
    cur = conn.cursor()
    print("Cursor created!")
    
    # Test executing a simple query
    cur.execute("SELECT current_database()")
    result = cur.fetchone()
    print(f"Current database: {result[0]}")
    
    # Close connections
    cur.close()
    conn.close()
    print("Connection closed properly.")
except Exception as e:
    print(f"Error: {e}")

print("Script finished...")