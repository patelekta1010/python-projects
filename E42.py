import pandas as pd

df=pd.read_csv('mydata.csv',names=['pizza','cat','dog'],header=0)
print(df)
cs = pd.read_csv('mydata.csv', usecols=[0, 1])
print(cs)

