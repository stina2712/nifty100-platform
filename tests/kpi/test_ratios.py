from src.analytics.ratios import get_leverage_flags

def test_leverage_flags():
    # Test High Leverage Flag
    hl, _ = get_leverage_flags(6.0, 'Manufacturing', 2.0)
    assert hl is True
    
    # Test ICR Warning Flag
    _, icr_warn = get_leverage_flags(1.0, 'Manufacturing', 1.2)
    assert icr_warn is True
    
    # Test Financial Sector suppression
    hl, _ = get_leverage_flags(6.0, 'Financials', 2.0)
    assert hl is False