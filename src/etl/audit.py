import sqlite3
import pandas as pd
import os

def run_day05_audit():
    db_path = 'nifty100.db'
    conn = sqlite3.connect(db_path)
    
    # Define expected row counts
    targets = {'companies': 92, 'profitandloss': 1276, 'balancesheet': 1312, 'cashflow': 1187, 'stock_prices': 5520}
    
    audit_data = []
    print("--- Running Day 05 Audit ---")
    
    for table, target in targets.items():
        count = pd.read_sql(f"SELECT COUNT(*) as count FROM {table}", conn).iloc[0,0]
        audit_data.append({'table': table, 'actual': count, 'expected': target})
        print(f"Table: {table} | Actual: {count} | Target: {target}")

    # Check Foreign Keys
    fk_check = pd.read_sql("PRAGMA foreign_key_check", conn)
    fk_errors = len(fk_check)
    print(f"\nForeign Key Violations: {fk_errors} (Expected: 0)")
    
    # Save audit to output folder
    os.makedirs('output', exist_ok=True)
    pd.DataFrame(audit_data).to_csv('output/load_audit.csv', index=False)
    conn.close()

if __name__ == "__main__":
    run_day05_audit()