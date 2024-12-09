import os
import subprocess

# Directory containing the Python files
directory = os.path.dirname(os.path.abspath("C:/Users/Ramro/OneDrive/Documents/Library/SJSU Semester 1 Material/team project Career Con/codes/data_generator/applicant.py"))

# List all files in the directory
files = os.listdir(directory)

# Filter out only Python files
python_files = [f for f in files if f.endswith('.py') and f != 'run_all.py']

# Run each Python file sequentially
for python_file in python_files:
    file_path = os.path.join(directory, python_file)
    print(f"Running {file_path}...")
    result = subprocess.run(['python', file_path], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    print(f"Finished running {file_path}\n")