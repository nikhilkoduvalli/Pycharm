import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/assignment/custom.txt',header=None)
df.columns=['id','name','age','loc','salary']
print(df)

df1=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/assignment/order.txt',header=None)
df1.columns=['oder_id','purchased_date','id','purchased_amound']
print(df1)

df3=pd.merge(df,df1,on='id',how='inner')
print(df3)

df4=df3.loc[df3['age']>25] [['name','age','loc','purchased_date','purchased_amound']]
print(df4)

df5=df3.sort_values(by='age',ascending=False) \
    [['name','age','loc','purchased_date','purchased_amound']].head(1)
print(df5)


df6=df3.sort_values(by='purchased_date',ascending=False) \
    [['name','age','salary','purchased_date','purchased_amound']].head(1)
print(df6)

