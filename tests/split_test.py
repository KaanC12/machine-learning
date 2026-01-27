from data import load
from data import split
import pytest
import pandas as pd



@pytest.fixture
def fake_df():
    return pd.DataFrame({
        "taster_name": ["A", "B", "C", "D", "E"],
        "country": ["USA"] * 5,
        "province": ["CA"] * 5,
        "region_1": ["Napa"] * 5,
        "region_2": ["Valley"] * 5,
        "variety": ["Merlot"] * 5,
        "price": [10, 20, 30, 40, 50],
        "winery": ["Y"] * 5,
        "points": [80, 85, 90, 95, 100]
    })

def test_create_set(monkeypatch, fake_df):
    def moc_load():
        return fake_df
    
    monkeypatch.setattr("data.load._load_database", moc_load)
    
    df = split.create_set()

    assert len(df) == 5

def test_random_split(monkeypatch, fake_df):
    def mock_load():
        return fake_df
    
    monkeypatch.setattr("data.load._load_database", mock_load)
    result = split.random_split()

    assert isinstance(result, dict)

    assert "train" in result
    assert "test" in result

    train = result["train"]
    test = result["test"]

    assert len(train) + len(test) == len(fake_df)

    assert len(train) == int(len(fake_df) * 0.8)
    assert len(test) == len(fake_df) - len(train)

    assert train.index.name == "taster_name"
    assert test.index.name == "taster_name"
    