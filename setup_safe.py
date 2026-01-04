import subprocess
import os
import sys

def install():
    print("Installing Node.js dependencies...")
    try:
        # shell=False bypasses the shell wrapper issues
        subprocess.run(['npm', 'install'], check=True, shell=False)
        print("Dependencies installed.")
    except Exception as e:
        print(f"Failed to install dependencies: {e}")
        print("Please run 'npm install' manually.")

def check_structure():
    print("Checking file structure...")
    if not os.path.exists('src/backend/logic.py'):
        print("Missing logic.py!")
    if not os.path.exists('src/tui/index.js'):
        print("Missing index.js!")
    print("Structure looks okay.")

if __name__ == "__main__":
    check_structure()
    install()
