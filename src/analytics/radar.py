import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_radar_charts(db_path):
    conn = sqlite3.connect(db_path)
    # Load your updated peer_percentiles table
    df = pd.read_sql("SELECT * FROM peer_percentiles", conn)
    os.makedirs("reports/radar_charts", exist_ok=True)
    
    # Dynamically find all columns ending in '_percentile'
    metrics = [col for col in df.columns if col.endswith('_percentile')]
    
    if not metrics:
        print("❌ No percentile columns found in the database. Run peer.py first!")
        return

    print(f"📊 Generating charts for metrics: {metrics}")
    
    for _, row in df.iterrows():
        # Get peer average for this group
        peer_group = row['peer_group_name']
        peer_avg = df[df['peer_group_name'] == peer_group][metrics].mean().values
        company_values = row[metrics].values
        
        # Setup Plot
        N = len(metrics)
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1] # Close the loop
        
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        
        # Company Polygon
        values = np.append(company_values, company_values[0])
        ax.plot(angles, values, 'o-', linewidth=2, label=row['company_name'])
        ax.fill(angles, values, alpha=0.25)
        
        # Peer Average Outline
        avg_values = np.append(peer_avg, peer_avg[0])
        ax.plot(angles, avg_values, '--', linewidth=2, label='Peer Avg')
        
        # Formatting
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(metrics, size=8)
        plt.title(f"{row['company_name']} vs {peer_group} Avg", size=12, y=1.1)
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        
        # Save
        filename = f"reports/radar_charts/{str(row['company_name']).replace(' ', '_')}_radar.png"
        plt.savefig(filename, bbox_inches='tight')
        plt.close()

    print(f"✅ Success! Radar charts saved in reports/radar_charts/")
    conn.close()

if __name__ == "__main__":
    generate_radar_charts('nifty100.db')