import sqlite3
import pandas as pd
from pathlib import Path

def bootstrap():
    print("🔄 Bootstrapping database and master table from raw files...")
    
    db_path = Path("db/nifty100.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Locate raw company file (adjust name if your source file differs)
    raw_companies_path = Path("data/raw/companies.xlsx")
    if not raw_companies_path.exists():
        raw_companies_path = Path("data/processed/companies.csv") # Fallback check
        
    if raw_companies_path.suffix == ".xlsx":
        df_companies = pd.read_excel(raw_companies_path)
    else:
        df_companies = pd.read_csv(raw_companies_path)
        
    # Standardize column names if needed
    df_companies.columns = [c.strip().lower().replace(" ", "_") for c in df_companies.columns]
    
    # Save master table CSV
    master_csv = output_dir / "final_master_table.csv"
    df_companies.to_csv(master_csv, index=False)
    print(f"✅ Generated {master_csv}")
    
    # Load into SQLite database
    with sqlite3.connect(db_path) as conn:
        df_companies.to_sql("companies", conn, if_exists="replace", index=False)
        print("✅ Created and populated 'companies' table in SQLite database.")

if __name__ == "__main__":
    bootstrap()