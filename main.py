import subprocess
import os

def run_pipeline():
    venv_python = os.path.join(os.getcwd(), 'venv', 'Scripts', 'python.exe')
    scripts = ['src/etl/validator.py', 'src/etl/transformer.py', 'src/etl/merger.py']
    
    for script in scripts:
        print(f"--- Running {script} ---")
        subprocess.run([venv_python, script], check=True)
    
    print("✅ Pipeline Update Complete. Master table is ready!")

if __name__ == "__main__":
    run_pipeline()