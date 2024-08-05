import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')


# Insert data
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 25))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 30))

conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Update data
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (26, 'Alice'))

conn.commit()

# Delete data
cursor.execute('DELETE FROM users WHERE name = ?', ('Bob',))

conn.commit()
conn.close()
