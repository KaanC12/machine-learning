import pandas as pd
import pytest
from data import load

@pytest.fixture
def fake_df():
    return pd.DataFrame({
        "taster_name": ["Daniel", "Virjidth", "Kağan", "Virjidth"],
        "points": [90, 95, 80, 70],
        "price": [20, 30, 15, 5]
    })

@pytest.fixture
def mock_load_database(monkeypatch, fake_df):
    def _mock(index_col=None):
        if index_col == "taster_name":
            return fake_df.set_index(index_col)
        return fake_df
    monkeypatch.setattr(load, "_load_database", _mock)


def test_get_columns(mock_load_database):
    cols = load.get_columns()
    assert set(cols) == {"taster_name", "points", "price"}

def test_get_sommelier_info_valid(mock_load_database):
    info = load.get_sommelier_info("Daniel")
    assert isinstance(info, list)
    assert len(info) == 2

def test_get_sommelier_info_invalid(mock_load_database):
    with pytest.raises(ValueError):
        load.get_sommelier_info("Ahmet")

def test_get_feature_info(mock_load_database):
    points = load.get_feature_info("points")
    assert points == [90, 95, 80, 70]

def test_get_top_rated_wines_by_sommelier(mock_load_database):
    top = load.get_top_rated_wines_by_sommelier("Virjidth", n=1)
    assert top[0] == 70