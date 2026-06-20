import pytest
from src.etl.loader import normalize_ticker, normalize_year

@pytest.mark.parametrize("input,expected", [
    ("infy", "INFY"),
    ("  tcs  ", "TCS"),
    ("HDFC ", "HDFC"),
])
def test_normalize_ticker(input, expected):
    assert normalize_ticker(input) == expected

@pytest.mark.parametrize("input,expected", [
    ("FY2025", 2025),
    ("2024-25", 2024),
    ("2026", 2026),
])
def test_normalize_year(input, expected):
    assert normalize_year(input) == expected