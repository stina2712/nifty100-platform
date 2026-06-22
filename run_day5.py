import sqlite3
import pandas as pd
from src.etl.loader import run_etl

# 1. Run the ETL
run_etl()

# 2. Force the Audit to look at the same path
db_path = r'C:\Users\HP\nifty100-platform\nifty100.db'
conn = sqlite3.connect(db_path)

tables = [
    'companies', 'profitandloss', 'balancesheet', 'cashflow', 
    'stock_prices', 'sectors', 'financial_ratios', 'market_cap', 'peer_groups'
]
audit = []

for table in tables:
    try:
        count = pd.read_sql(f"SELECT COUNT(*) FROM {table}", conn).iloc[0,0]
        audit.append({'table': table, 'row_count': count})
    except Exception as e:
        print(f"❌ Error auditing {table}: {e}")

pd.DataFrame(audit).to_csv(r'C:\Users\HP\nifty100-platform\output\load_audit.csv', index=False)
conn.close()
print("✅ Done. Audit saved.")