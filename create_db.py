import sqlite3

conn = sqlite3.connect("database.db")  # your database file
cur = conn.cursor()

# Create registrations table
cur.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    service TEXT,
    reason TEXT
)
""")

# Optional: create enquiries table if not already created
cur.execute("""
CREATE TABLE IF NOT EXISTS enquiries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    mobile TEXT,
    address TEXT,
    source TEXT
)
""")

# Optional: create admin table
cur.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.commit()
conn.close()
print("✅ Tables created successfully!")