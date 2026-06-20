import pandas as pd

def get_top_performers():
    # Load master file
    master_df = pd.read_excel('data/master/nifty100_master.xlsx')
    
    # 1. Filter for the latest year (assuming your year column is numeric)
    latest_year = master_df['year'].max()
    latest_df = master_df[master_df['year'] == latest_year]
    
    # 2. Sort by Net Profit
    top_5 = latest_df.sort_values(by='net_profit', ascending=False).head(5)
    
    print(f"--- Top 5 Companies by Net Profit ({latest_year}) ---")
    print(top_5[['company_name', 'net_profit']])

if __name__ == "__main__":
    get_top_performers()