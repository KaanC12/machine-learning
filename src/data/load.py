import pandas as pd
import os

def load_database(index_col=None):
    data_path = os.getenv("DATA_PATH")
    return pd.read_csv(data_path, index_col=index_col)

def get_columns() -> list[str]:
    df = load_database()
    return df.columns.to_list()


