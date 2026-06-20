import pandas as pd
import os

# Configuration
RAW_DATA_PATH = 'data/raw'
OUTPUT_PATH = 'output'
all_failures = []

def run_dq_checks(df, table_name, valid_company_ids):
    failures = []
    
    # --- DQ-01: Primary Key Uniqueness ---
    # Companies file uses 'id', others use 'company_id'
    key_col = 'id' if 'id' in df.columns else 'company_id'
    
    if key_col in df.columns:
        if df[key_col].duplicated().any():
            failures.append({'table': table_name, 'rule': 'DQ-01', 'msg': 'Duplicate ID found'})

    # --- DQ-03: Foreign Key Integrity ---
    if 'company_id' in df.columns:
        invalid_ids = df[~df['company_id'].isin(valid_company_ids)]['company_id'].unique()
        if len(invalid_ids) > 0:
            failures.append({'table': table_name, 'rule': 'DQ-03', 'msg': f'Invalid company_ids found: {invalid_ids}'})
            
    return failures

def main():
    print("--- Starting Validation Suite ---")
    
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    
    # 1. Load Master Company List
    master_path = os.path.join(RAW_DATA_PATH, 'companies.xlsx')
    master_df = pd.read_excel(master_path, header=1)
    master_df.columns = master_df.columns.str.strip().str.lower()
    valid_company_ids = master_df['id'].unique()
    
    # 2. Loop through files
    for filename in os.listdir(RAW_DATA_PATH):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(RAW_DATA_PATH, filename)
            
            df = pd.read_excel(file_path, header=1)
            df.columns = df.columns.str.strip().str.lower()
            
            file_failures = run_dq_checks(df, filename, valid_company_ids)
            all_failures.extend(file_failures)
            print(f"Validated {filename}...")

    # 3. Final Report
    if all_failures:
        output_df = pd.DataFrame(all_failures)
        output_df.to_csv(os.path.join(OUTPUT_PATH, 'validation_failures.csv'), index=False)
        print(f"FAILED: Validation complete. {len(all_failures)} issues saved to output/validation_failures.csv")
    else:
        print("SUCCESS: Validation complete. No data quality issues found!")

if __name__ == "__main__":
    main()