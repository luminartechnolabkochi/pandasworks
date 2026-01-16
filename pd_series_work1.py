import pandas as pd

# pd.Series(data)
data=[165,163,167,170,164]
#      0   1   2    3  4

series = pd.Series(data)

print(series)

# create weight series create lst with weight of 10 peoples 
# convert that into series

# head() list top 5 record
# tail() last 5 record
print(series.head())

print(series.tail())

print(series.shape)

