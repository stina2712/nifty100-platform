import sqlite3
import pandas as pd
from src.screener.engine import get_preset_results

# 1. Load data
conn = sqlite3.connect('nifty100.db')
df = pd.read_sql("SELECT * FROM financial_ratios", conn)
conn.close()

# 2. Define list of presets
presets = [
    "Quality Compounder", "Value Pick", "Growth Accelerator", 
    "Dividend Champion", "Debt-Free Blue Chip", "Turnaround Watch"
]

# 3. Print counts
print(f"{'Preset Name':<20} | {'Count':<5}")
print("-" * 30)
for p in presets:
    results = get_preset_results(df, p)
    print(f"{p:<20} | {len(results):<5}")