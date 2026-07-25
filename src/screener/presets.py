from pathlib import Path
from src.screener.engine import run_screener

PRESETS_DIR = Path("output/presets")
PRESETS_DIR.mkdir(parents=True, exist_ok=True)

def generate_preset_screeners():
    presets = {
        "quality_compounder.csv": {
            "min_roce": 15.0,
            "max_de": 0.5,
            "min_profit_cagr": 10.0,
            "min_sales_cagr": 8.0
        },
        "value_pick.csv": {
            "min_roce": 12.0,
            "max_de": 1.0,
            "min_profit_cagr": 5.0
        },
        "low_debt_engine.csv": {
            "max_de": 0.1,
            "min_roce": 10.0
        }
    }

    results = {}
    for filename, criteria in presets.items():
        df = run_screener(**criteria)
        output_path = PRESETS_DIR / filename
        df.to_csv(output_path, index=False)
        results[filename] = len(df)
        print(f"Generated {filename} with {len(df)} matching companies.")
        
    return results

if __name__ == "__main__":
    generate_preset_screeners()