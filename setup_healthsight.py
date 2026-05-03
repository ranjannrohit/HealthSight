import os

# Project root folder
project_name = "HealthSight"
folders = [
    "data/raw",
    "data/cleaned",
    "notebooks",
    "scripts"
]

# Files to create
files = [
    "README.md",
    ".gitignore",
    "notebooks/Week1_Data_Loading.ipynb",
    "scripts/data_cleaning.py"
]

# Create folders
for folder in folders:
    path = os.path.join(project_name, folder)
    os.makedirs(path, exist_ok=True)
    print(f"Created folder: {path}")

# Create empty files
for file in files:
    path = os.path.join(project_name, file)
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass
        print(f"Created file: {path}")