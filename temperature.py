#max()-




import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/pycham/Temperature1',sep=' ',header=None)
df.columns=['year','temp']
print(df)
print('*'*100)
df1=df.groupby('year') ['temp'].max() \
    .sort_values(ascending=False)
print(df1)


#min()-


print('*'*100)
df2=df.groupby('year') ['temp'].min() \
    .sort_values(ascending=False)
print(df2)

#sum()



print('*'*100)
df3=df.groupby('year') ['temp'].sum() \
    .sort_values(ascending=False)
print(df3)



#mean()

print('*'*100)
df3=df.groupby('year') ['temp'].mean() \
    .sort_values(ascending=False)
print(df3)







