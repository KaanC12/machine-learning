from data import clean, encode
import pandas as pd

FEATURE_COLUMNS = [
    "country",
    "province",
    "region_1",
    "region_2",
    "variety",
    "winery"
]

def implement_encode(taster_name: str):
    features = encode.get_mean_encoding()
    train_data = clean.get_taster_data_train(taster_name)
    test_data = clean.get_taster_data_test(taster_name)

    for col in FEATURE_COLUMNS:
        train_data[col] = train_data[col].map(features[col])
        test_data[col] = test_data[col].map(features[col])

    return {
        "train_data": train_data,
        "test_data": test_data
    }