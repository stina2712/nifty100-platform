from src.etl.loader import load_data_to_db

tables = [
    ('data/companies.xlsx', 'companies'),
    ('data/sectors.xlsx', 'sectors'),
    ('data/profitandloss.xlsx', 'profitandloss'),
    ('data/balancesheet.xlsx', 'balancesheet'),
    ('data/cashflow.xlsx', 'cashflow'),
    ('data/stock_prices.xlsx', 'stock_prices'),
    # Add other files here if you have them
]

for file, table in tables:
    load_data_to_db(file, table)