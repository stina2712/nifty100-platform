def generate_company_summary(company):
    """
    Analyzes company data using .get() to prevent crashes when 
    specific financial columns are missing.
    """
    # Safely retrieve data; defaults to 0 if the column is missing
    revenue = company.get('revenue', 0)
    net_profit = company.get('net_profit', 0)
    # The .get() method is the key to stopping your 'borrowings' error
    borrowings = company.get('borrowings', 0) 
    equity = company.get('equity', 0)
    
    # Calculate metrics
    profit_margin = (net_profit / revenue * 100) if revenue and revenue != 0 else 0
    debt_to_equity = (borrowings / equity) if equity and equity != 0 else 0
    
    return {
        "profit_margin_percent": round(profit_margin, 2),
        "debt_to_equity_ratio": round(debt_to_equity, 2),
        "status": "Calculated"
    }