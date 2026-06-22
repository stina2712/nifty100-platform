import sqlite3
import pandas as pd
import os

def get_top_performing_companies():
    # Construct the path to the database in the root folder
    db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'nifty100.db')
    
    conn = sqlite3.connect(db_path)
    
    # Query to get top 5 companies by ROE
    query = """
    SELECT id, roe_percentage 
    FROM companies 
    ORDER BY roe_percentage DESC 
    LIMIT 5
    """
    
    try:
        df = pd.read_sql(query, conn)
        print("--- Top 5 Companies by ROE ---")
        print(df)
    except Exception as e:
        print(f"Error querying database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    get_top_performing_companies()