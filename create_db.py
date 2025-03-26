import sqlite3
import pandas as pd

# Load Excel file (Change filename if needed)
excel_file = "fs.xml.xlsx"

# Connect to SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usn TEXT UNIQUE,
    name TEXT,
    project_title TEXT,
    guide TEXT
)
""")

# Read data from Excel
df = pd.read_excel(excel_file)

# Insert data into database
for _, row in df.iterrows():
    cursor.execute("INSERT OR IGNORE INTO students (usn, name, project_title, guide) VALUES (?, ?, ?, ?)",
                   (row["USN"], row["Name"], row["Project Title"], row["Guide"]))

# Commit and close
conn.commit()
conn.close()

print("✅ Database Created & Data Inserted!")
