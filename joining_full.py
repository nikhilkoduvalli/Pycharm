import numpy as np
import pandas as pd

df=pd.read_csv("/Users/nikhi/OneDrive/my/Desktop/assignment/custom.txt",header=None)
df.columns=['id','name','age','location','salary']
print(df)

df1=pd.read_csv("/Users/nikhi/OneDrive/my/Desktop/assignment/order.txt",header=None)
df1.columns=['order_id','order_date','id','amount']
print(df1)


df3=pd.merge(df,df1,on='id',how='left')
print(df3)


df5=df3.loc[df3['salary']>15000]
print(df5)