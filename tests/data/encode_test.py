import pytest
import pandas as pd
from data import load
from data import encode

@pytest.fixture
def fake_df():
    return pd.DataFrame({
        "country": ["USA", "USA", "FR"],
        "province": ["CA", "CA", "IDF"],
        "region_1": ["Napa", "Napa", "Paris"],
        "region_2": ["Valley", "Valley", "Center"],
        "variety": ["Merlot", "Merlot", "Cabernet"],
        "price": [10, 20, 30],
        "winery": ["A", "A", "B"],
        "points": [90, 80, 70]
    })


@pytest.fixture
def mock_load_database(monkeypatch, fake_df):
    def _mock(index_col=None):
        if index_col:
            return fake_df.set_index(index_col)
        return fake_df
    
    monkeypatch.setattr("data.load._load_database", _mock)

def test_get_numerical_values_country(mock_load_database):
    result = encode._get_numerical_values("country", "USA")

    assert len(result) == 2
    assert result[0] == "USA"
    assert result[1] == (90 + 80) / 2