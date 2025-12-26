import pandas as pd
from src.paths import SYNTHETIC_DATA

# headings are taken from : documentation_code.ipynb so that u can match and understand from teh notebook


######################################################################## 2.b Saving Data 

def save_synthetic_data(df: pd.DataFrame) -> None: 
    """
    Saves the synthetic dataset to data folder.
    folder : data/syntheticData/universal_synthetic_data.csv
    """
    df.to_csv(SYNTHETIC_DATA, index=False)

######################################################################## 2.b Extracting Data 

def load_synthetic_data() -> pd.DataFrame:
    """
    Loads the synthetic dataset from data folder.
    folder : data/syntheticData/universal_synthetic_data.csv
    """
    return pd.read_csv(SYNTHETIC_DATA)
