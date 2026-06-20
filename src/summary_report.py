import pandas as pd
import os

# Load exactly as we did in the merger
df = pd.read_excel('data/processed/sectors.xlsx', header=None, skiprows=10)

print("--- Inspecting the first 5 rows of sectors.xlsx ---")
for i in range(df.shape[1]):
    print(f"Column {i} sample values: {df[i].dropna().unique()[:3]}")