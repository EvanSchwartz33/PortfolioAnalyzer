import sqlite3

def create_tables():
    # Connect to SQLite database (or create it if it doesn't exist)
    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    # SQL commands to create the tables
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR NOT NULL,
        hashed_password VARCHAR NOT NULL,
        salt VARCHAR NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        
    );
    """

    create_stocks_table = """
    CREATE TABLE IF NOT EXISTS stocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker VARCHAR NOT NULL,
        user_id INTEGER NOT NULL,
        avg_purchase_price FLOAT,
        shares VARCHAR NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """

    # Execute the SQL commands
    cursor.execute(create_users_table)
    cursor.execute(create_stocks_table)

    # Commit changes and close the con
    con.commit()
    con.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")