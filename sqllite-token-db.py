import sqlite3


def create_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT NOT NULL
    )
    ''')

    # Insert a sample user (you can replace with your own credentials)
    cursor.execute('''
    INSERT INTO users (username, password, token)
    VALUES ('user1', 'password123', 'secret_token_1')
    ''')

    connection.commit()
    connection.close()


create_db()
