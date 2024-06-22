import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

logging.info("Hello Everyone. welcome to this course.")

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating the directory {filedir} for the files {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath))==0:
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating the empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")


