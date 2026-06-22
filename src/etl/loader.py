import pandas as pd
import sqlite3
import os

def run_etl():
    db_path = r'C:\Users\HP\nifty100-platform\nifty100.db'
    if os.path.exists(db_path): os.remove(db_path)
    conn = sqlite3.connect(db_path)
    
    # Path to your raw data
    base_path = r'C:\Users\HP\nifty100-platform\data\raw'
    
    files = {
        'companies': os.path.join(base_path, 'companies.xlsx'),
        'profitandloss': os.path.join(base_path, 'profitandloss.xlsx'),
        'balancesheet': os.path.join(base_path, 'balancesheet.xlsx'),
        'cashflow': os.path.join(base_path, 'cashflow.xlsx'),
        'stock_prices': os.path.join(base_path, 'stock_prices.xlsx'),
        'sectors': os.path.join(base_path, 'sectors.xlsx'),
        'financial_ratios': os.path.join(base_path, 'financial_ratios.xlsx'),
        'market_cap': os.path.join(base_path, 'market_cap.xlsx'),
        'peer_groups': os.path.join(base_path, 'peer_groups.xlsx')
    }
    
    for table, path in files.items():
        if os.path.exists(path):
            # Using header=1 to skip the first row of metadata
            df = pd.read_excel(path, header=1)
            
            # Clean column names: lowercase, strip whitespace, replace spaces with underscores
            df.columns = [str(c).lower().strip().replace(' ', '_').replace('&', 'and') for c in df.columns]
            
            df.to_sql(table, conn, if_exists='replace', index=False)
            print(f"✅ Loaded {table} with columns: {list(df.columns)}")
        else:
            print(f"❌ File NOT FOUND: {path}")
            
    conn.close()
    print("--- ETL Process Complete ---")

if __name__ == "__main__":
    run_etl()