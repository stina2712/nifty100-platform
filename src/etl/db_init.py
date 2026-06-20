import sqlite3
import os

def create_database():
    # Define paths
    db_path = 'nifty100.db'
    schema_path = 'db/schema.sql'
    
    # Remove old db if it exists to ensure a clean slate
    if os.path.exists(db_path):
        os.remove(db_path)
        
    conn = sqlite3.connect(db_path)
    with open(schema_path, 'r') as f:
        conn.executescript(f.read())
    
    conn.commit()
    conn.close()
    print("✅ nifty100.db created successfully with 10 tables.")

if __name__ == "__main__":
    create_database()