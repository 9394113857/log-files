import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
''')
conn.commit()

# Insert a test user
cursor.execute('''
    INSERT INTO users (username, password)
    VALUES (?, ?)
''', ('testuser', 'testpassword'))
conn.commit()

conn.close()
