import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/sql/student.unknown',sep=',',header=None)
df.columns=['name','rollno']
print(df)

df.to_csv('/Users/nikhi/OneDrive/my/Desktop/sql/student.csv',index=False)


