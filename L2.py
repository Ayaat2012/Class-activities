import pandas as pd
import numpy as np

mydataset = {
    'cars': ['BMW', 'Mercedes', 'Tesla'],
    'passings': [3,7,4]
}

df1 = pd.DataFrame(mydataset)
print(df1)
df = pd.DataFrame(mydataset, index=[1,2,3])
print(df)

print(df.iloc[0,[0,1]])
print(df.loc[1,['cars', "passings"]])


#SERIES
a = [1,2,3]
ser1 = pd.Series(a)
print(ser1)
ser = pd.Series([1,2,3], index=['a','b','c'])
print(ser)
ser2 = pd.Series({"day1": 520, "day2": 390, "day3": 230})
print(ser2)


# LOAD FILES
df = pd.read_csv("Countries Data.csv")
print(df.head())
print(df.info())
print("Is null:", df.isnull().sum())
df.dropna(inplace=True)
print("Is null:", df.isnull().sum())
print(df.head())

#print(df_new)
#To fill in a "null" place in a table:
#print(df.filna(subset = ["year"], value = 1930, inplace=True))