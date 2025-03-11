import psycopg2

print("Script starting...")

def connect_to_db():
    conn = psycopg2.connect(
        host='mlb-the-show-db.clw2io0soo2o.us-east-2.rds.amazonaws.com',
        database='mlb-the-show-db',
        user='skeebo',
        password='ChicagoBearsSP24!',
        port='5432'
    )
    print("Database connection successful!")
    return conn

def create_user_table():
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL
        );
        """

        cur.execute(create_table_query)
        conn.commit()
        print("Users table created successfully.")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error creating table: {e}")

def example_query():
    try:
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM users LIMIT 5")

        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data found in users table.")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error querying table: {e}")

# Make sure these functions are called
create_user_table()
example_query()

print("Script finished...")