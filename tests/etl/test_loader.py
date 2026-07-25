import os
import pandas as pd
import sqlite3

# Define standard paths
CSV_PATH = 'output/final_master_table.csv'
DB_PATH = 'nifty100.db'

def get_all_company_data():
    """Load and return all company data from the master CSV file."""
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    print(f"❌ Error: {CSV_PATH} not found. Check your 'output' folder.")
    raise FileNotFoundError(f"❌ Error: {CSV_PATH} not found. Check your 'output' folder.")

def normalize_ticker(ticker: str) -> str:
    """Normalize company ticker symbols."""
    if not isinstance(ticker, str):
        return ""
    return ticker.strip().upper()

def normalize_year(year) -> int:
    """Normalize financial year formats."""
    try:
        return int(str(year).strip())
    except (ValueError, TypeError):
        return 0

def load_data_to_db():
    """Load the processed master table into the SQLite database."""
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: {CSV_PATH} not found. Check your 'output' folder.")
        return
    
    df = pd.read_csv(CSV_PATH)
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('financial_ratios', conn, if_exists='replace', index=False)
    conn.close()
    print("Successfully loaded data into nifty100.db")

if __name__ == "__main__":
    load_data_to_db()