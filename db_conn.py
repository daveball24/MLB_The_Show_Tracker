import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host = 'mlb-the-show-db.clw2io0soo2o.us-east-2.rds.amazonaws.com',
        database = 'mlb-the-show-db',
        user = 'skeebo',
        password = 'ChicagoBearsSP24!',
        port = '5432'
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

    cur.executre("SELECT * FROM your_table LIMIT 5")

    rows = cur.fetchall()
    for row in rows:
        print(rows)

    cur.close()
    conn.close()
