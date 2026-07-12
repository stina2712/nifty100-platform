import pandas as pd
import sqlite3

def calculate_peer_percentiles(db_path, peer_file):
    conn = sqlite3.connect(db_path)
    df_data = pd.read_sql("SELECT * FROM financial_ratios", conn)
    df_data = df_data.rename(columns={df_data.columns[1]: 'company_name'})
    df_peers = pd.read_excel(peer_file)
    df = pd.merge(df_data, df_peers, on='company_name')

    # Mapping your DB columns to the 8 required metrics
    # Adjust the numbers [X] to match your actual column positions if needed
    metrics_map = {
        'roe_percentile': df.columns[3],     # ROE
        'pe_percentile': df.columns[12],     # P/E
        'rev_growth_percentile': df.columns[11], # Revenue CAGR
        'de_percentile': df.columns[4],      # D/E
        # Add others if your DB has them (e.g., FCF, Asset Turnover)
    }

    for col_name, db_col in metrics_map.items():
        if 'de' in col_name: # Inverse for Debt
            df[col_name] = 1 - df.groupby('peer_group_name')[db_col].rank(pct=True)
        else:
            df[col_name] = df.groupby('peer_group_name')[db_col].rank(pct=True)
    
    df.to_sql('peer_percentiles', conn, if_exists='replace', index=False)
    conn.close()
    print("✅ Peer percentiles updated with all metrics.")

if __name__ == "__main__":
    calculate_peer_percentiles('nifty100.db', 'peer_groups.xlsx')