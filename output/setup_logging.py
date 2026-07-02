import logging

# Configure logging
logging.basicConfig(filename='output/ratio_edge_cases.log', level=logging.INFO)

def log_anomaly(company_name, metric, computed_val, source_val):
    diff = abs(computed_val - source_val)
    if diff > 5: # Threshold from Day 13 requirements
        logging.info(f"Anomaly: {company_name} | Metric: {metric} | Diff: {diff}%")