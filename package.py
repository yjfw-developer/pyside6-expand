import os
import subprocess
import sys

if __name__ == '__main__':
    python_executable = sys.executable
    setup_script_path = "setup.py"
    command = [python_executable, setup_script_path, "sdist"]
    result = subprocess.run(command, check=True)

    os.system("twine upload dist/*")

