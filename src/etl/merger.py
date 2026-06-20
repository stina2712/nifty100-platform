import pandas as pd
import os

PROCESSED_PATH = 'data/processed'

def merge_data():
    print("--- Starting Final Relational Merge ---")
    ROW_OFFSET = 10 
    
    # Load files
    pnl = pd.read_excel(os.path.join(PROCESSED_PATH, 'profitandloss.xlsx'), header=None, skiprows=ROW_OFFSET)
    sect = pd.read_excel(os.path.join(PROCESSED_PATH, 'sectors.xlsx'), header=None, skiprows=ROW_OFFSET)

    # Prepare PNL: Ticker (1), Sales (9), Net Profit (10)
    df_pnl = pnl.iloc[:, [1, 9, 10]].copy()
    df_pnl.columns = ['ticker', 'sales', 'net_profit']
    
    # Prepare Sectors: Ticker (1), Broad Sector (2)
    df_sect = sect.iloc[:, [1, 2]].copy()
    df_sect.columns = ['ticker', 'broad_sector']

    # Normalize tickers for consistent matching
    df_pnl['ticker'] = df_pnl['ticker'].astype(str).str.strip().str.upper()
    df_sect['ticker'] = df_sect['ticker'].astype(str).str.strip().str.upper()

    # Perform the Relational Join
    # This matches the 'ticker' column from PNL to the 'ticker' column in Sectors
    master = pd.merge(df_pnl, df_sect, on='ticker', how='left')
    
    master.to_excel('data/master/nifty100_master.xlsx', index=False)
    
    # Final check: How many matches did we actually find?
    matches = master['broad_sector'].notna().sum()
    print(f"✅ Merge complete. Total rows: {len(master)}")
    print(f"✅ Successfully matched {matches} rows to a Sector.")

if __name__ == "__main__":
    merge_data()