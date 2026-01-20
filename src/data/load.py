import pandas as pd
import os

def load_database(index_col=None):
    data_path = os.getenv("DATA_PATH")
    return pd.read_csv(data_path, index_col=index_col)

def get_columns() -> list[str]:
    df = load_database()
    return df.columns.to_list()


def get_sommelier_info(sommelier_name: str) -> list[str]:
    df = load_database(index_col="taster_name")
    tasters = df.index.to_list()
    if sommelier_name not in tasters:
        raise RuntimeError("There is not such a sommelier")
    
    return df.loc[sommelier_name].to_list()

    