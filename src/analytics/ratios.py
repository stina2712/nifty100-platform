import logging

# Configure logging (you can put this at the top of your file)
logging.basicConfig(filename='output/ratio_edge_cases.log', level=logging.WARNING)

def check_opm_variance(computed_opm, reported_opm, ticker):
    if reported_opm is None:
        return True # Cannot cross-check if data is missing
    
    if abs(computed_opm - reported_opm) > 1.0:
        logging.warning(f"OPM Mismatch for {ticker}: Computed={computed_opm:.2f}%, Reported={reported_opm:.2f}%")
        return False
    return True