def classify_capital_allocation(cfo, cfi, cff):
    # Pattern Logic
    if cfo > 0 and cfi < 0 and cff < 0:
        return "Mature / Dividend Payer"
    elif cfo > 0 and cfi < 0 and cff > 0:
        return "Growth / Expander"
    elif cfo < 0 and cfi < 0 and cff > 0:
        return "Early Stage / Startup"
    return "Complex / Mixed"

def calculate_cfo_quality(cfo_sum, pat_sum):
    if pat_sum == 0:
        return None
    return (cfo_sum / pat_sum)