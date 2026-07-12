import sqlite3
import pandas as pd
from engine import get_preset_results # Ensure your engine functions are exported

conn = sqlite3.connect('nifty100.db')
df = pd.read_sql("SELECT * FROM financial_ratios", conn)

presets = ["Quality Compounder", "Value Pick", "Growth Accelerator"] 

for p in presets:
    results = get_preset_results(df, p)
    print(f"{p}: {len(results)} companies found.")