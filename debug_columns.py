import sqlite3
import pandas as pd

conn = sqlite3.connect('nifty100.db')
tables = ['companies', 'profitandloss']

for table in tables:
    # This queries the SQLite schema to get real column names
    cols = pd.read_sql(f"PRAGMA table_info({table})", conn)
    print(f"\n--- Columns in '{table}' ---")
    print(cols['name'].tolist())

conn.close()