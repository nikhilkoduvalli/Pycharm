import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/sql/customer5.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc','salary']
print(df)

df.to_csv('/Users/nikhi/OneDrive/my/Desktop/sql/customer5.csv')