import sqlite3
import pandas as pd
import os

# Ensure this matches your pipeline output filename
csv_path = 'output/final_master_table.csv' 
db_path = 'nifty100.db'

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    # The screener engine expects these specific columns
    df.to_sql('financial_ratios', conn, if_exists='replace', index=False)
    conn.close()
    print("✅ Step 1: Database populated successfully.")
else:
    print(f"❌ Error: {csv_path} not found. Check your 'output' folder.")