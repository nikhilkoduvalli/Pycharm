


import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/pycham/customer51.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc','salary']
print(df)
print('*'*100)


df1=df.groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(df1)
print('*'*100)

df1=df.groupby('prof') ['age'].max() \
    .sort_values(ascending=False)
print(df1)
print('*'*100)


df1=df.groupby('prof') ['salary'].min() \
    .sort_values(ascending=False)
print(df1)
print('*'*100)


df1=df.groupby('age') ['salary'].mean() \
    .sort_values(ascending=False)
print(df1)
print('*'*100)


df1=df.groupby('prof') ['salary'].sum() \
    .sort_values(ascending=False)
print(df1)
print('*'*100)
