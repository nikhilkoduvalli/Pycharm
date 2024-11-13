import numpy as np
import pandas as pd
df=pd.read_csv("/Users/nikhi/Downloads/sample4.txt",sep=",",header=None)
df.columns=["id","fname","lname","age","phno","loc"]
print(df)


print("*"*100)
print(df.head(3))
print("*"*100)
print(df.dtypes)
print("*"*100)

df1=df[['fname','lname','age','phno']]

print(df1)
print("*"*100)

df2=df[['fname','lname','age']].head(2)
print(df2)
