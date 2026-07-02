# src/analytics/ratios.py

def calculate_de_ratio(data):
    """Calculates D/E and returns (ratio, flag)."""
    borrowings = data.get('borrowings', 0)
    equity_base = data.get('equity', 0) + data.get('reserves', 0)
    sector = data.get('broad_sector', '')
    
    if equity_base <= 0: return 0, False
    
    ratio = round(borrowings / equity_base, 2)
    high_leverage_flag = (ratio > 5 and sector != 'Financials')
    
    return ratio, high_leverage_flag

def calculate_icr(data):
    """Calculates Interest Coverage Ratio."""
    op_profit = data.get('op_profit', 0)
    other_income = data.get('other_income', 0)
    interest = data.get('interest_expense', 0)
    
    if not interest or interest == 0:
        return None # Day 09: Return None for debt-free
    return round((op_profit + other_income) / interest, 2)

def calculate_asset_turnover(data):
    """Calculates Asset Turnover."""
    revenue = data.get('revenue', 0)
    assets = data.get('total_assets', 0)
    
    if not assets or assets == 0:
        return None
    return round(revenue / assets, 2)