from src.analytics.cashflow import classify_capital_allocation, calculate_cfo_quality

def test_cashflow_classification():
    # Test Mature pattern: (+, -, -)
    assert classify_capital_allocation(100, -50, -20) == "Mature / Dividend Payer"
    
    # Test Growth pattern: (+, -, +)
    assert classify_capital_allocation(100, -50, 20) == "Growth / Expander"
    
    # Test Startup pattern: (-, -, +)
    assert classify_capital_allocation(-50, -100, 200) == "Early Stage / Startup"

def test_cfo_quality():
    assert calculate_cfo_quality(100, 100) == 1.0
    assert calculate_cfo_quality(50, 100) == 0.5
    assert calculate_cfo_quality(100, 0) is None