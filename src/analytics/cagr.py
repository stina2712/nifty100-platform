def calculate_cagr(start, end, n):
    if n < 1 or start is None or end is None:
        return None, "INSUFFICIENT"
    
    if start == 0:
        return None, "ZERO_BASE"
    
    # 6-Edge Case Logic
    if start > 0 and end > 0:
        return ((end / start) ** (1/n) - 1) * 100, "NORMAL"
    elif start > 0 and end < 0:
        return None, "DECLINE_TO_LOSS"
    elif start < 0 and end > 0:
        return None, "TURNAROUND"
    elif start < 0 and end < 0:
        return None, "BOTH_NEGATIVE"
    
    return None, "UNKNOWN"