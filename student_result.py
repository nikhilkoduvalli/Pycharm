import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/assignment/student.txt',header=None)
df.columns=['name','rollno']
print(df)

df1=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/assignment/results.txt',header=None)
df1.columns=['rollno','result']
print(df1)

df3=pd.merge(df,df1,on='rollno',how='inner')
print(df3)

df4=df3.loc[df3['result']=='pass'] [['name','rollno','result']]
print(df4)
