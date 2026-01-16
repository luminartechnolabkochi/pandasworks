
import pandas as pd

student_total={"s1":450,"s2":475,"s3":490,"s4":485}


series = pd.Series(student_total)

print(series["s3"])

# create a employee dictionary and convert that to series

# aggregate functions
# sum()
# max()
# min()
# mean()

print("total",series.sum())

print("max",series.max())