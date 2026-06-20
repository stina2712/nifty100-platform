import pandas as pd
import re

def normalize_ticker(ticker):
    """Strips whitespace and converts to uppercase."""
    if pd.isna(ticker):
        return None
    return str(ticker).strip().upper()

def normalize_year(year_val):
    """Extracts a 4-digit year from various string formats."""
    if pd.isna(year_val):
        return None
    # Regex to find a 4-digit number (e.g., 2025 from "FY2025" or "2025-26")
    match = re.search(r'\d{4}', str(year_val))
    return int(match.group()) if match else None

def load_excel_data(file_path):
    """Loads and normalises raw data."""
    df = pd.read_excel(file_path)
    if 'ticker' in df.columns:
        df['ticker'] = df['ticker'].apply(normalize_ticker)
    if 'year' in df.columns:
        df['year'] = df['year'].apply(normalize_year)
    return df