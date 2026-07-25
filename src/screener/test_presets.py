import sqlite3
import pandas as pd
from src.screener.engine import get_preset_results  # Fixed import path

conn = sqlite3.connect('nifty100.db')
df = pd.read_sql("SELECT * FROM financial_ratios", conn)

presets = ["Quality Compounder", "Value Pick", "Growth Accelerator"] 

for p in presets:
    results = get_preset_results(df, p)
    print(f"{p}: {len(results)} companies found.")