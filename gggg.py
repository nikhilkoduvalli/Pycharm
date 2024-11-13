import pandas as pd
df1=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/sql/results.unknown',sep=',',header=None)
df1.columns=['rollno','result']
print(df1)

df1.to_csv('/Users/nikhi/OneDrive/my/Desktop/sql/results.csv',index=False)
