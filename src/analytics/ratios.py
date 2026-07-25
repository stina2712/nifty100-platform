import sqlite3
import pandas as pd
from pathlib import Path

def save_ratios():
    db_path = Path("db/nifty100.db")
    
    # Check if we have final master data to compute or load ratios from
    master_path = Path("output/final_master_table.csv")
    if not master_path.exists():
        print("❌ Error: output/final_master_table.csv not found.")
        return

    df = pd.read_csv(master_path)
    
    # If your script generates specific ratio columns, ensure they map correctly.
    # Here we create/ensure columns exist for database insertion to prevent schema misses:
    expected_cols = [
        "company_id", "roce", "debt_to_equity", 
        "profit_cagr_3yr", "sales_cagr_3yr", 
        "current_ratio", "interest_coverage"
    ]
    
    # Fill missing columns with dummy defaults if your ratio engine builds them dynamically
    for col in expected_cols:
        if col not in df.columns:
            df[col] = 0.0 # Default fallback if column is missing

    with sqlite3.connect(db_path) as conn:
        df[expected_cols].to_sql("financial_ratios", conn, if_exists="replace", index=False)
        print("✅ Successfully wrote 'financial_ratios' table to database.")

if __name__ == "__main__":
    save_ratios()