import pytest
from src.etl.loader import get_all_company_data, normalize_ticker, normalize_year

def test_get_all_company_data_structure():
    """Verify the loader returns a list of dictionaries."""
    data = get_all_company_data()
    
    # Check if it returned a list
    assert isinstance(data, list)
    
    # If the database has data, verify the first item is a dictionary
    if len(data) > 0:
        assert isinstance(data[0], dict)

@pytest.mark.parametrize("input, expected", [
    ("infy", "INFY"),
    (" tcs ", "TCS"),
    ("HDFC ", "HDFC"),
])
def test_normalize_ticker(input, expected):
    assert normalize_ticker(input) == expected

@pytest.mark.parametrize("input, expected", [
    ("2025", 2025),
    (2024, 2024),
])
def test_normalize_year(input, expected):
    assert normalize_year(input) == expected