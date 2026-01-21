import pandas as pd
from data import load

FEATURE_COLUMNS = [
    "taster_name",
    "country",
    "province",
    "region_1",
    "region_2",
    "variety",
    "price",
    "winery",
    "points"
]

# Creates a data frame from desired features.
def create_set() -> pd.DataFrame:
    db = pd.DataFrame({})
    df = load._load_database()

    db = df[FEATURE_COLUMNS]
    db = db.set_index("taster_name")

    return db

# Shuffels the dataset.    
def random_split() -> dict:
    df = create_set()
    df = df.sample(frac=1, random_state=42)

    n = len(df)
    n_80 = int(n * 0.8)
    train = df.iloc[:n_80]
    test = df.iloc[n_80:]
    
    return {
        "train": train,
        "test": test
    }