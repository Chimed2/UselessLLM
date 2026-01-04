import os
import subprocess
import sys

def run_command(command, cwd=None):
    try:
        # Explicitly use bash to avoid fish syntax issues in the shell wrapper if possible,
        # otherwise run directly.
        subprocess.run(command, cwd=cwd, check=True, shell=True, executable='/bin/bash')
        print(f"Successfully ran: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {command}: {e}")
    except Exception as e:
        print(f"Execution failed: {e}")

def create_dirs():
    os.makedirs('src/backend', exist_ok=True)
    os.makedirs('src/tui', exist_ok=True)
    print("Directories created.")

def install_node_deps():
    # Attempt to install node modules
    if os.path.exists('package.json'):
        run_command('npm install')

if __name__ == "__main__":
    create_dirs()
    install_node_deps()
