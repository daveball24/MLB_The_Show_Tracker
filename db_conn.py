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
    return conn

def create_user_table():
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

    cur.close()
    conn.close()

    print("Users table created successfully.")

def example_query():
    conn = connect_to_db()
    cur = conn.cursor()

    # Fixed typo: executre → execute
    cur.execute("SELECT * FROM users LIMIT 5")  # Also fixed table name case: Users → users

    rows = cur.fetchall()
    for row in rows:
        # Fixed: print(rows) → print(row)
        print(row)

    cur.close()
    conn.close()

# Added function calls to make the script do something
if __name__ == "__main__":
    try:
        create_user_table()
        example_query()
    except Exception as e:
        print(f"An error occurred: {e}")

print("Script finished...")