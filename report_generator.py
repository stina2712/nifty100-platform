import pandas as pd
import os

def generate_summary():
    # 1. Define the path to your master file
    master_path = 'data/master/nifty100_master.xlsx'
    
    if not os.path.exists(master_path):
        print(f"Error: {master_path} not found. Did you run merger.py first?")
        return

    # 2. Load the data
    df = pd.read_excel(master_path)
    
    # 3. Generate the summary
    print("\n--- 📊 Sector Performance Summary ---")
    summary = df.groupby('broad_sector')[['sales', 'net_profit']].sum()
    
    # 4. Print and optionally save
    print(summary)
    summary.to_excel('data/master/sector_summary.xlsx')
    print("\n✅ Summary saved to: data/master/sector_summary.xlsx")

if __name__ == "__main__":
    generate_summary()