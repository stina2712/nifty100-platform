import pytest
from src.analytics.ratios import calculate_npm, calculate_opm, calculate_roe, calculate_roce, calculate_roa

def test_profitability_calculations():
    # Normal cases
    assert calculate_npm(10, 100) == 10.0
    assert calculate_opm(20, 100) == 20.0
    assert calculate_roe(10, 50, 50) == 10.0
    assert calculate_roce(20, 40, 40, 20) == 20.0 # 20 / 100
    assert calculate_roa(10, 200) == 5.0

    # Edge cases (Zero denominator)
    assert calculate_npm(10, 0) is None
    assert calculate_roe(10, -50, 40) is None # Equity base -10
    assert calculate_roce(10, 0, 0, 0) is None # Capital employed 0