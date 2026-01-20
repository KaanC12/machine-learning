import pandas as pd
import os

# Loads the database.
def _load_database(index_col=None):
    data_path = os.getenv("DATA_PATH")
    return pd.read_csv(data_path, index_col=index_col)

# Checks whether the sommelier present.
def _is_sommelier_present(sommelier_name: str) -> bool:
    df = _load_database(index_col="taster_name")
    return sommelier_name in df.index

# Returns all the columns.
def get_columns() -> list[str]:
    df = _load_database()
    return df.columns.to_list()

# Returns information about sommelier.
def get_sommelier_info(sommelier_name: str) -> list[str]:
    df = _load_database(index_col="taster_name")
    
    if not _is_sommelier_present(sommelier_name):
        raise ValueError("There is not such a sommelier.")
    
    return df.loc[sommelier_name].to_list()

# Returns information about each feature.
def get_feature_info(feature: str) -> list[str]:
    df = _load_database()
    return df[feature].to_list()

# Returns top rated wines by a somelier.
def get_top_rated_wines_by_sommelier(sommelier_name: str, n=10) -> list[int]: 
    df = _load_database(index_col="taster_name")
    if not _is_sommelier_present(sommelier_name):
        raise ValueError("There is not such a sommelier.")
    return df.loc[sommelier_name, "points"].sort_values().head(10).to_list()