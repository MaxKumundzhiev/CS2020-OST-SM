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

account_chars: str = digits + ascii_letters


def _random_account_id() -> str:
    """Return a random account number made of 12 characters."""
    return "".join(choices(account_chars, k=12))


def _random_amount() -> float:
    """Return a random amount between 1.00 and 1000.00."""
    return randint(100, 1000000) / 100


def create_random_transaction() -> dict:
    """Create a fake, randomised transaction."""
    return {
        "source": _random_account_id(),
        "target": _random_account_id(),
        "amount": _random_amount(),
        # Keep it simple: it's all euros
        "currency": "EUR",
    }


def validate_dataset(dataset) -> Path:
    dataset_path = Path(f'/usr/src/app/NAS/{dataset}/test/test.csv')
    assert dataset_path.exists(), f'FileNotFound, there is no such {dataset} file or directory'
    return dataset_path


def get_dataset(dataset_path: str) -> List[dict]:
    df = pd.read_csv(dataset_path)
    assert df.empty is False, 'Dataset is empty'
    return df.to_dict(orient='records')

