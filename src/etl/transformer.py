import pandas as pd
import os

RAW_PATH = 'data/raw'
PROCESSED_PATH = 'data/processed'

# Ensure the processed folder exists
os.makedirs(PROCESSED_PATH, exist_ok=True)

def clean_data():
    # 1. Load Master IDs (to filter against)
    master_df = pd.read_excel(os.path.join(RAW_PATH, 'companies.xlsx'), header=1)
    master_df.columns = master_df.columns.str.strip().str.lower()
    valid_ids = master_df['id'].unique()
    
    print("--- Starting Transformation ---")
    
    for filename in os.listdir(RAW_PATH):
        if filename.endswith(".xlsx"):
            # Load
            df = pd.read_excel(os.path.join(RAW_PATH, filename), header=1)
            df.columns = df.columns.str.strip().str.lower()
            
            # 2. Apply Transformation (Example: Filter valid company_ids)
            if 'company_id' in df.columns:
                initial_count = len(df)
                df = df[df['company_id'].isin(valid_ids)]
                print(f"Cleaned {filename}: Removed {initial_count - len(df)} invalid records.")
            
            # 3. Save to processed folder
            df.to_excel(os.path.join(PROCESSED_PATH, filename), index=False)

if __name__ == "__main__":
    clean_data()
    print("--- Transformation Complete ---")