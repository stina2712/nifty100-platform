import sqlite3
import os

def get_all_company_data():
    """Fetches all rows from the profitandloss database table."""
    db_path = 'nifty100.db'
    
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file {db_path} not found!")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    table_name = 'profitandloss' 
    
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        data = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return data
    except sqlite3.OperationalError as e:
        conn.close()
        raise Exception(f"Database error: {e}. Ensure table '{table_name}' exists.")

def normalize_ticker(ticker):
    return str(ticker).strip().upper()

def normalize_year(year):
    return int(year)