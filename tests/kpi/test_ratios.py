import pytest
from src.analytics.ratios import calculate_de_ratio, calculate_icr, calculate_asset_turnover

def test_de_ratio_calculation():
    # Test normal case
    data = {'borrowings': 100, 'equity': 100, 'reserves': 50, 'broad_sector': 'Tech'}
    ratio, flag = calculate_de_ratio(data)
    assert ratio == 0.67  # 100 / 150 rounded

def test_de_ratio_debt_free():
    # Test Day 09: Borrowings 0 should return 0
    data = {'borrowings': 0, 'equity': 100, 'reserves': 50, 'broad_sector': 'Tech'}
    ratio, flag = calculate_de_ratio(data)
    assert ratio == 0

def test_icr_zero_interest():
    # Test Day 09: Interest 0 returns None
    data = {'op_profit': 100, 'other_income': 10, 'interest_expense': 0}
    assert calculate_icr(data) is None

def test_asset_turnover_zero_assets():
    # Test Day 09: Assets 0 returns None
    data = {'revenue': 1000, 'total_assets': 0}
    assert calculate_asset_turnover(data) is None