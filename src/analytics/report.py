import pandas as pd
import sqlite3
import xlsxwriter

def generate_peer_report(db_path, output_path="output/peer_comparison.xlsx"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM peer_percentiles", conn)
    
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    workbook = writer.book
    
    # Define colors
    green = workbook.add_format({'bg_color': '#C6EFCE'})  # >= 75th
    yellow = workbook.add_format({'bg_color': '#FFEB9C'}) # 25th - 75th
    red = workbook.add_format({'bg_color': '#FFC7CE'})    # <= 25th

    for group in df['peer_group_name'].unique():
        subset = df[df['peer_group_name'] == group]
        subset.to_excel(writer, sheet_name=str(group)[:31], index=False)
        worksheet = writer.sheets[str(group)[:31]]
        
        # Apply conditional formatting to percentile columns
        for i, col in enumerate(subset.columns):
            if 'percentile' in col:
                col_letter = chr(65 + i)
                range_str = f"{col_letter}2:{col_letter}100"
                worksheet.conditional_format(range_str, {'type': 'cell', 'criteria': '>=', 'value': 0.75, 'format': green})
                worksheet.conditional_format(range_str, {'type': 'cell', 'criteria': 'between', 'minimum': 0.25, 'maximum': 0.75, 'format': yellow})
                worksheet.conditional_format(range_str, {'type': 'cell', 'criteria': '<', 'value': 0.25, 'format': red})
    
    writer.close()
    conn.close()
    print(f"✅ Peer Comparison report generated: {output_path}")

if __name__ == "__main__":
    generate_peer_report('nifty100.db')