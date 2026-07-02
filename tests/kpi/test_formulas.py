# tests/kpi/test_formulas.py
import pytest
from src.analytics.ratios import calculate_de_ratio, calculate_icr

def test_de_ratio_debt_free():
    # Test Day 09: Borrowings 0 should return 0
    data = {'borrowings': 0, 'equity': 100, 'reserves': 50, 'broad_sector': 'Tech'}
    ratio, flag = calculate_de_ratio(data)
    assert ratio == 0

def test_icr_zero_interest():
    # Test Day 09: Interest 0 returns None
    data = {'op_profit': 100, 'other_income': 10, 'interest_expense': 0}
    assert calculate_icr(data) is None

def test_high_leverage_flag():
    # Test Day 09: D/E > 5 flag should be True
    data = {'borrowings': 600, 'equity': 100, 'reserves': 0, 'broad_sector': 'Tech'}
    ratio, flag = calculate_de_ratio(data)
    assert flag is True