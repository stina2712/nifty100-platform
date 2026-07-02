# src/analytics/cashflow_kpis.py

def classify_capital_allocation(cfo, cfi, cff):
    """
    Classifies capital allocation based on signs (+, -) of Cash Flows.
    """
    # Logic: CFO=Operating, CFI=Investing, CFF=Financing
    # Signs represented as tuples
    signs = (cfo > 0, cfi > 0, cff > 0)
    
    mapping = {
        (True, False, False): "Reinvestor",
        (True, True, False): "Liquidating Assets",
        (False, True, True): "Distress Signal",
        (False, False, True): "Growth Funded by Debt",
        (True, True, True): "Cash Accumulator",
        (False, False, False): "Pre-Revenue",
        (True, False, True): "Mixed"
    }
    
    return mapping.get(signs, "Unknown")