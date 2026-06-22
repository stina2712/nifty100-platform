import sqlite3
import pandas as pd
from src.etl.loader import run_etl

print("--- 1. Starting ETL ---")
run_etl()

print("--- 2. Running Audit ---")
conn = sqlite3.connect('nifty100.db')
targets = {'companies': 92, 'profitandloss': 1276, 'balancesheet': 1312, 'cashflow': 1187}

audit = []
for table, target in targets.items():
    count = pd.read_sql(f"SELECT COUNT(*) FROM {table}", conn).iloc[0,0]
    audit.append({'table': table, 'actual': count, 'target': target})

pd.DataFrame(audit).to_csv('output/load_audit.csv', index=False)
conn.close()
print("✅ Audit complete. Check output/load_audit.csv")