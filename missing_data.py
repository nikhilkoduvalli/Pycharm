import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/Downloads/missing_data.csv',sep=',')
print(df)





print("*"*100)
df1=df[['Duration','Date','Pulse','Maxpulse']].head(5)
print(df1)
print("*"*100)
df2=df[['Date','Pulse','Maxpulse']].tail(5)
print(df2)
print("*"*100)


print(df.isna().sum())
print("*"*100)



df3=df.fillna('None')
print(df3.isna().sum())