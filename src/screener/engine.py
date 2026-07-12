import sqlite3
import pandas as pd
import os
import xlsxwriter

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'nifty100.db')
    return sqlite3.connect(db_path)

def get_preset_results(df, preset_name):
    # Mapping indices to names
    col_map = {
        df.columns[3]: 'roe_pct',
        df.columns[4]: 'de_ratio',
        df.columns[5]: 'fcf',
        df.columns[11]: 'revenue_cagr_5yr',
        df.columns[12]: 'pe_ratio',
        df.columns[13]: 'pb_ratio',
        df.columns[14]: 'dividend_yield',
        df.columns[15]: 'market_cap_cr'
    }
    df = df.rename(columns=col_map)
    
    # Ensure numeric
    for col in ['roe_pct', 'de_ratio', 'fcf', 'revenue_cagr_5yr', 'pe_ratio', 'pb_ratio', 'dividend_yield', 'market_cap_cr']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    if preset_name == "Quality Compounder":
        return df[(df['roe_pct'] >= 15.0) & (df['fcf'] > 0) & (df['revenue_cagr_5yr'] > 10.0)]
    elif preset_name == "Value Pick":
        return df[(df['pe_ratio'] < 20.0) & (df['pb_ratio'] < 3.0) & (df['dividend_yield'] > 1.0)]
    elif preset_name == "Debt-Free Blue Chip":
        return df[(df['de_ratio'] < 0.1) & (df['market_cap_cr'] > 50000) & (df['roe_pct'] >= 15.0)]
    elif preset_name == "Growth Accelerator":
        return df[(df['revenue_cagr_5yr'] > 20.0)]
    elif preset_name == "Dividend Champion":
        return df[(df['dividend_yield'] > 3.0) & (df['roe_pct'] > 12.0)]
    elif preset_name == "Turnaround Watch":
        return df[(df['de_ratio'] < 1.0)]
    return pd.DataFrame()

def compute_composite_score(df):
    df['composite_score'] = (
        (df['roe_pct'].fillna(0).clip(0, 30) / 30 * 35) + 
        (df['revenue_cagr_5yr'].fillna(0).clip(0, 30) / 30 * 20) +
        ((1 / (df['de_ratio'].fillna(0) + 0.1)).clip(0, 10) * 15)
    ).clip(0, 100)
    return df.sort_values(by='composite_score', ascending=False)

def generate_excel_report(all_results, output_path="output/screener_output.xlsx"):
    os.makedirs("output", exist_ok=True)
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    workbook = writer.book
    
    green = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
    red = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    
    for preset_name, df in all_results.items():
        df = compute_composite_score(df)
        df.to_excel(writer, sheet_name=preset_name[:31], index=False)
        worksheet = writer.sheets[preset_name[:31]]
        
        # Apply formatting to ROE column (Column D)
        worksheet.conditional_format('D2:D1000', {'type': 'cell', 'criteria': '>=', 'value': 15, 'format': green})
        worksheet.conditional_format('D2:D1000', {'type': 'cell', 'criteria': '<', 'value': 15, 'format': red})
        
    writer.close()
    print(f"✅ Generated {output_path}")

if __name__ == "__main__":
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM financial_ratios", conn)
    conn.close()
    
    presets = ["Quality Compounder", "Value Pick", "Debt-Free Blue Chip", 
               "Growth Accelerator", "Dividend Champion", "Turnaround Watch"]
    results_map = {p: get_preset_results(df.copy(), p) for p in presets}
    
    generate_excel_report(results_map)