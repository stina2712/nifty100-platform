import sqlite3
import pandas as pd

def review_data():
    conn = sqlite3.connect('nifty100.db')
    
    # 1. Fetch 5 random companies
    print("--- Checking 5 Random Companies ---")
    companies = pd.read_sql("SELECT id, company_name FROM companies ORDER BY RANDOM() LIMIT 5", conn)
    print(companies)
    
    # 2. Check year coverage in Profit & Loss
    # We use 'company_id' as the link between tables
    ids = tuple(companies['id'].tolist())
    query = f"""
    SELECT company_id, COUNT(year) as year_count 
    FROM profitandloss 
    WHERE company_id IN {ids} 
    GROUP BY company_id
    """
    coverage = pd.read_sql(query, conn)
    print("\n--- Year Coverage (Should be ~5 years) ---")
    print(coverage)
    
    # 3. Check for companies with < 5 years of data
    low_data = pd.read_sql("SELECT company_id, COUNT(year) as years FROM profitandloss GROUP BY company_id HAVING years < 5", conn)
    print(f"\n--- Companies with less than 5 years of data: {len(low_data)} ---")
    
    conn.close()

if __name__ == "__main__":
    review_data()