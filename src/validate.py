import os
import sqlite3

def validate_sprint3():
    print("--- 🛡️ Sprint 3 Validation Report ---")
    
    # 1. Check Output Files
    files = ["output/screener_output.xlsx", "output/peer_comparison.xlsx"]
    for f in files:
        status = "✅ Found" if os.path.exists(f) else "❌ Missing"
        print(f"File {f}: {status}")
    
    # 2. Check Database Tables
    db_path = 'nifty100.db'
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [t[0] for t in cursor.fetchall()]
        print(f"Database Tables: {tables}")
        conn.close()
    else:
        print("❌ Database file not found!")
    
    # 3. Check Radar Charts
    radar_dir = 'reports/radar_charts/'
    radar_count = len(os.listdir(radar_dir)) if os.path.exists(radar_dir) else 0
    print(f"Radar Charts Generated: {radar_count}")
    
    print("--- Validation Complete ---")

if __name__ == "__main__":
    validate_sprint3()