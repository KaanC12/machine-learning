import matplotlib.pyplot as plt
from data.load import get_columns, get_feature_info


def visualize_dataset():
    print(get_columns())

    countries = get_feature_info("country")

    names = []
    counts = []

    for c in countries:
        if c in names:
            i = names.index(c)
            counts[i] = counts[i] + 1
        else:
            names.append(c)
            counts.append(1)

    plt.bar(names, counts)
    plt.title("Wine Count by Country")
    plt.xticks(rotation=90)
    plt.show()

    points = get_feature_info("points")

    plt.hist(points, bins=20)
    plt.title("Wine Ratings")
    plt.show()

    prices = get_feature_info("price")
    clean_prices = []

    for p in prices:
        if p == p:
            clean_prices.append(p)

    plt.hist(clean_prices, bins=30)
    plt.title("Wine Prices")
    plt.show()


visualize_dataset()
