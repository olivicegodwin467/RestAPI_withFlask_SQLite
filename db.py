import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("books.sqlite")
cursor = conn.cursor()

# SQL query to create the 'books' table if it doesn't already exist
book_queries = """
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    author TEXT NOT NULL,
    language TEXT NOT NULL,
    title TEXT NOT NULL
)
"""

# Execute the SQL query
cursor.execute(book_queries)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Database created with its tables.")
