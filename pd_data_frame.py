"""
DataFrame is like 2d array in numpy with rows and columns

"""
import pandas as pd

students={
    "name":["adhnan","adhil","risen","rafi","jibin"],
    "age":[23,21,25,26,25],
    "course":["ds","ds","dj","st","ds"]
}


df = pd.DataFrame(students)

# print(df[1:2]) 

print(df["course"])

print(df[["name","age"]])