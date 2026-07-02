import pytest
from src.analytics.cagr import calculate_cagr

def test_cagr_scenarios():
    # Normal Case
    val, flag = calculate_cagr(100, 200, 5)
    assert flag == "NORMAL"
    
    # Edge Cases
    assert calculate_cagr(100, -50, 5)[1] == "DECLINE_TO_LOSS"
    assert calculate_cagr(-100, 50, 5)[1] == "TURNAROUND"
    assert calculate_cagr(-100, -50, 5)[1] == "BOTH_NEGATIVE"
    assert calculate_cagr(0, 50, 5)[1] == "ZERO_BASE"