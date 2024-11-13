import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/sql/Temperature1.txt',sep=' ',header=None)
df.columns=['year','temp']
print(df)

df.to_csv('/Users/nikhi/OneDrive/my/Desktop/sql/Temperature2.csv',index=False)