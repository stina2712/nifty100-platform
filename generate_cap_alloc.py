import json
import csv

with open('output/nifty100_analysis.json', 'r') as f:
    data = json.load(f)

with open('output/capital_allocation.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['company_id', 'year', 'cfo_sign', 'cfi_sign', 'cff_sign', 'pattern_label'])
    for row in data:
        # Based on your Day 11 logic
        writer.writerow([row.get('company_id'), row.get('year'), 
                         row.get('cfo_sign'), row.get('cfi_sign'), row.get('cff_sign'), 
                         row.get('pattern_label')])