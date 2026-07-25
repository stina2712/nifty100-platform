import subprocess
import sys
from pathlib import Path

def run_command(command):
    print(f"\n▶ Running: {' '.join(command)}")
    result = subprocess.run(command, text=True)
    if result.returncode != 0:
        print(f"❌ Error executing {' '.join(command)}")
        sys.exit(result.returncode)

def main():
    print("🚀 Starting Nifty 100 Analytics Pipeline Execution...")
    
    Path("output/presets").mkdir(parents=True, exist_ok=True)
    Path("db").mkdir(exist_ok=True)
    
    # Step 0: Bootstrap database and tables from raw files
    run_command([sys.executable, "-m", "src.etl.bootstrap_db"])
    
    # Step 1: Run ETL loader
    run_command([sys.executable, "-m", "src.etl.loader"])
    
    # Step 2: Run Ratios Engine
    run_command([sys.executable, "-m", "src.analytics.ratios"])
    
    # Step 3: Run Screener Presets
    run_command([sys.executable, "-m", "src.screener.presets"])
    
    print("\n✅ Pipeline executed successfully! Check the 'output/presets' folder for results.")

if __name__ == "__main__":
    main()