import sqlite3

def run_spot_check():
    conn = sqlite3.connect('db/nifty100.db')
    cursor = conn.cursor()
    # Check if we hit the 1100+ row requirement
    cursor.execute("SELECT COUNT(*) FROM financial_ratios")
    count = cursor.fetchone()[0]
    print(f"Total Rows Verified: {count}")
    
    # Pull 3 companies for manual verification
    cursor.execute("SELECT company_name, roe_pct, revenue_cagr_5yr FROM financial_ratios LIMIT 3")
    print(cursor.fetchall())

if __name__ == "__main__":
    run_spot_check()