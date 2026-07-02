import json
import os
from src.etl.loader import get_all_company_data
from src.analytics.summary_report import generate_company_summary

def run_analytics_pipeline():
    print("Loading data...")
    all_companies = get_all_company_data()
    
    if not all_companies:
        print("No data found.")
        return
        
    final_reports = []
    print(f"Processing {len(all_companies)} companies...")
    
    for company in all_companies:
        # Use .get() even here to ensure the merge doesn't fail
        # if the input dictionary itself is missing the key
        insights = generate_company_summary(company)
        
        # Merge dictionary
        report = {**company, **insights}
        final_reports.append(report)
        
    if not os.path.exists('output'):
        os.makedirs('output')
        
    with open('output/nifty100_analysis.json', 'w') as f:
        json.dump(final_reports, f, indent=4)
        
    print(f"Pipeline complete: {len(final_reports)} reports saved.")