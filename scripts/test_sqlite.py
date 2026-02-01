import sqlite3
import os

db_file = 'test.db'
# Remove existing db to ensure clean state for the test
if os.path.exists(db_file):
    os.remove(db_file)

try:
    # Connect to database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table
    cursor.execute('CREATE TABLE test_db (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)')
    print("Table 'test_db' created.")

    # Insert data
    cursor.execute("INSERT INTO test_db (content) VALUES ('Hello Quant')")
    conn.commit()
    print("Inserted 'Hello Quant'.")

    # Read data
    cursor.execute('SELECT * FROM test_db')
    rows = cursor.fetchall()
    
    print("\nReading data:")
    for row in rows:
        print(f"ID: {row[0]}, Content: {row[1]}")

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
finally:
    if conn:
        conn.close()
