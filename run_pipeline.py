import sys
import os

# Add the current directory to sys.path to ensure 'src' can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.pipeline import run_analytics_pipeline

if __name__ == "__main__":
    print("Starting the data pipeline...")
    try:
        run_analytics_pipeline()
    except Exception as e:
        print(f"Pipeline failed: {e}")