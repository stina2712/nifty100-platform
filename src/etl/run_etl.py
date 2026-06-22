from src.etl.loader import load_data_to_db

# Add the rest of your tables here
tasks = [
    ('data/processed/companies.xlsx', 'companies'),
    ('data/processed/sectors.xlsx', 'sectors'),
    ('data/processed/profitandloss.xlsx', 'profitandloss'),
    ('data/processed/balancesheet.xlsx', 'balancesheet'),
    ('data/processed/cashflow.xlsx', 'cashflow'),
    ('data/processed/stock_prices.xlsx', 'stock_prices'),
    # ... add the others as needed
]

for file_path, table in tasks:
    load_data_to_db(file_path, table)