import logging
from src.analytics.ratios import calculate_de_ratio, calculate_icr, calculate_asset_turnover

# Configure logging for Day 13 anomaly tracking
logging.basicConfig(filename='output/ratio_edge_cases.log', level=logging.INFO, force=True)

def check_and_log_anomaly(company_name, metric_name, computed, source):
    """Logs discrepancies between computed and source data."""
    if source is not None and abs(computed - source) > 5:
        logging.info(f"Anomaly: {company_name} | {metric_name} | Computed: {computed} | Source: {source}")

def generate_company_summary(company):
    """
    Analyzes company data to generate KPIs.
    """
    # 1. Calculate ratios
    de_result = calculate_de_ratio(company)
    # Handle the tuple return from our updated ratios.py
    de_ratio = de_result[0] if isinstance(de_result, tuple) else de_result
    
    icr = calculate_icr(company)
    turnover = calculate_asset_turnover(company)
    
    # 2. Profitability Calculation
    revenue = company.get('revenue', 0)
    net_profit = company.get('net_profit', 0)
    margin = (net_profit / revenue * 100) if revenue and revenue != 0 else 0
    
    # 3. Construct the report
    return {
        "net_profit_margin_pct": round(margin, 2),
        "debt_to_equity": de_ratio,
        "interest_coverage": icr,
        "asset_turnover": turnover,
        "status": "Calculated"
    }