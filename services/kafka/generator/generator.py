# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

from pathlib import Path
from typing import List
from random import choices, randint
from string import ascii_letters, digits

import pandas as pd


def validate_dataset(dataset) -> Path:
    dataset_path = Path(f'/usr/src/app/NAS/{dataset}/test/test.csv')
    assert dataset_path.exists(), f'FileNotFound, there is no such {dataset} file or directory'
    print(f'VALIDATED DATASET: {dataset_path}')
    return dataset_path


def get_dataset(dataset_path: str) -> List[dict]:
    df = pd.read_csv(dataset_path)
    assert df.empty is False, 'Dataset is empty'
    print(f'READ DATASET: {dataset_path}')
    return df.to_dict(orient='records')

