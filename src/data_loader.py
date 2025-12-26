import pandas as pd
from src.paths import SYNTHETIC_DATA


def save_synthetic_data(df: pd.DataFrame) -> None:
    """
    Saves the synthetic dataset to data folder.
    """
    df.to_csv(SYNTHETIC_DATA, index=False)


def load_synthetic_data() -> pd.DataFrame:
    """
    Loads the synthetic dataset from data folder.
    """
    return pd.read_csv(SYNTHETIC_DATA)
