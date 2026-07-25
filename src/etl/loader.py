import sqlite3
import pandas as pd
from pathlib import Path
import streamlit as st

DB_PATH = Path("db/nifty100.db")
OUTPUT_DIR = Path("output")
OUTPUT_MASTER = OUTPUT_DIR / "final_master_table.csv"

def get_connection():
    """Creates and returns a SQLite database connection."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def load_data_to_db(file_path: str, table_name: str):
    """
    Loads a CSV file into the specified SQLite database table.
    Accepts file_path and table_name to match orchestrator calls.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"❌ Error: {file_path} not found. Check your file paths.")
    
    df = pd.read_csv(path)
    with get_connection() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Successfully loaded {file_path} into table '{table_name}'.")

@st.cache_data
def get_all_company_data() -> pd.DataFrame:
    """
    Retrieves the final master table data as a DataFrame, 
    ensuring output/final_master_table.csv exists.
    """
    if not OUTPUT_MASTER.exists():
        raise FileNotFoundError(f"❌ Error: {OUTPUT_MASTER} not found. Check your 'output' folder.")
    return pd.read_csv(OUTPUT_MASTER)

@st.cache_data
def load_sql_query(query: str) -> pd.DataFrame:
    """
    Executes a SQL query against the SQLite database and returns the result as a cached DataFrame.
    """
    if not DB_PATH.exists():
        raise FileNotFoundError(f"❌ Error: Database {DB_PATH} not found.")
    with get_connection() as conn:
        return pd.read_sql(query, conn)

def safe_load_query(query: str, fallback_message: str = "Unable to fetch data.") -> pd.DataFrame:
    """
    Safely executes a SQL query with built-in error handling for production apps.
    """
    try:
        return load_sql_query(query)
    except Exception as e:
        st.error(f"⚠️ {fallback_message} Details: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Example test execution if run directly
    print("Running loader module...")
    if OUTPUT_MASTER.exists():
        load_data_to_db(str(OUTPUT_MASTER), "final_master")
    else:
        print("Master table not yet generated. Run your ETL transformation script first.")