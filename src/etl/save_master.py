# In your save_master.py
def run_export():
    master_df = merge_data()
    
    # Force the correct column names
    master_df.columns = [
        'id', 'company_name', 'period', 'roe_pct', 'de_ratio', 'fcf', 
        'col6', 'col7', 'col8', 'col9', 'col10', 'revenue_cagr_5yr', 
        'pe_ratio', 'pb_ratio', 'dividend_yield', 'market_cap_cr'
    ]
    
    # Save with headers
    conn = sqlite3.connect('nifty100.db')
    master_df.to_sql('financial_ratios', conn, if_exists='replace', index=False)
    conn.close()
    print("Database updated with correct headers.")