def get_leverage_flags(de_ratio, sector, icr):
    # D/E Warning: High leverage for non-financials
    high_leverage_flag = False
    if sector != 'Financials' and de_ratio is not None and de_ratio > 5.0:
        high_leverage_flag = True
        
    # ICR Warning: Risk of not covering interest
    icr_warning_flag = False
    if icr is not None and icr < 1.5:
        icr_warning_flag = True
        
    return high_leverage_flag, icr_warning_flag