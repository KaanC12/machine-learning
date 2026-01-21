from data import split
import pandas as pd


# Returns the data related to one sommeiler.
def get_taster_data_train(taster_name: str) -> pd.DataFrame:
    data = split.random_split()
    df = data["train"]
    df = df.set_index("taster_name")
    if taster_name in df.index:
        return df.loc[taster_name]
    else:
        raise ValueError("The taster does not exist.")
    
# Returns the data related to one semmeiler.
def get_taster_data_test(taster_name: str) -> pd.DataFrame:
    data = split.random_split()
    df = data["test"]
    df = df.set_index("taster_name")
    if taster_name in df.index:
        return df.loc[taster_name]
    else:
        raise ValueError("The taster does not exist.")
