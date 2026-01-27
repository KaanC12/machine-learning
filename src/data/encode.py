from data import load

# Finds the numberical values of each features.
def _get_numerical_values(index_col: str, feature: str) -> list:
    df = load._load_database(index_col)
    rows = df.loc[[feature]]
    n = len(rows)
    total = df.loc[feature, "points"].sum()

    return [feature, float(total / n)]

# Returns the mean values of each input.
def get_mean_encoding():
    features = {}
    df = load._load_database("country")
    country_set = set(df.index.to_list())
    feature_country = {}
    for country in country_set:
        feature_country[country] = _get_numerical_values("country", country)[1]

    df = df.set_index("province")
    feature_province = {}
    province_set = set(df.index.to_list())
    for province in province_set:
        feature_province[province] = _get_numerical_values("province", province)[1]
    
    df = df.set_index("region_1")
    feature_region_1 = {}
    region_1_set = set(df.index.to_list())
    for region_1 in region_1_set:
        feature_region_1[region_1] = _get_numerical_values("region_1", region_1)[1]

    df = df.set_index("region_2")
    feature_region_2 = {}
    region_2_set = set(df.index.to_list())
    for region_2 in region_2_set:
        feature_region_2[region_2] = _get_numerical_values("region_2", region_2)[1]
    
    df = df.set_index("variety")
    feature_variety = {}
    variety_set = set(df.index.to_list())
    for variety in variety_set:
        feature_variety[variety] = _get_numerical_values("variety", variety)[1]
    
    df = df.set_index("price")
    feature_price = {}
    price_set = set(df.index.to_list())
    for price in price_set:
        feature_price[price] = _get_numerical_values("price", price)[1]

    df = df.set_index("winery")
    feature_winery = {}
    winery_set = set(df.index.to_list())
    for winery in winery_set:
        feature_winery[winery] = _get_numerical_values("winery", winery)[1]

    features["province"] = feature_province
    features["region_1"] = feature_region_1
    features["region_2"] = feature_region_2
    features["variety"] = feature_variety
    features["price"] = feature_price
    features["winery"] = feature_winery

    return features