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

def test_get_mean_encoding(mock_load_database):
    features = encode.get_mean_encoding()

    assert "province" in features
    assert "region_1" in features
    assert "region_2" in features
    assert "variety" in features
    assert "price" in features
    assert "winery" in features

    assert features["province"]["CA"] == (90 + 80) / 2
    assert features["province"]["IDF"] == 70

    assert features["region_1"]["Napa"] == (90 + 80) / 2
    assert features["region_1"]["Paris"] == 70

    assert features["variety"]["Merlot"] == (90 + 80) / 2
    assert features["variety"]["Cabernet"] == 70