import subprocess
import os
import sys

def run_pipeline():
    # Force the use of the Python executable inside your VENV
    venv_python = os.path.join(os.getcwd(), 'venv', 'Scripts', 'python.exe')
    
    scripts = [
        'src/etl/validator.py', 
        'src/etl/transformer.py', 
        'src/etl/merger.py'
    ]
    
    for script in scripts:
        print(f"--- Executing {script} ---")
        # Run using the explicit VENV python path
        result = subprocess.run([venv_python, script], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error in {script}:")
            print(result.stderr)
            break
        else:
            print(result.stdout)
            
    print("✅ Pipeline finished successfully!")

if __name__ == "__main__":
    run_pipeline()