import sqlite3

def create_tables():
    conn = sqlite3.connect('nifty100.db')
    cursor = conn.cursor()
    
    # Use IF NOT EXISTS to prevent errors on multiple runs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            ticker TEXT PRIMARY KEY,
            company_name TEXT,
            sector TEXT
        )
    ''')
    
    # Add other tables here...
    
    conn.commit()
    conn.close()
    print("✅ Database schema initialized.")

if __name__ == "__main__":
    create_tables()