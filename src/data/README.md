# Data
Before using the dataset, the important inputs, which are highyl affecting the points, should be selected. The important inputs are following:

1. taster_name
2. country
3. province
4. region_1
5. region_2
6. variety
7. price
8. winery
9. points

The inputs are divided by taster_name so that a sommeiler can be modeled. In order to do this, we are using the following pipeline:

1. Load
2. Split
3. Clean
4. Encoders
5. Tasters