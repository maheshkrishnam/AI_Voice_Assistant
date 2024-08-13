import os
import logging
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s: %(message)s]'
)

file_list = [
    'src/__init__.py',
    'src/helper.py',
    '.env',
    'requirements.txt',
    'setup.py',
    'app.py',
    'research/trials.ipynb'
]

for filepath in file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory : {filedir} for file : {filename}')
    
    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file : {filepath}')
            
    else:
        logging.info(f'{filename} already exists')