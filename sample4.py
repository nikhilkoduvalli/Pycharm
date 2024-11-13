import numpy as np
import pandas as pd

df=pd.read_csv("/Users/nikhi/Downloads/sample4.txt",sep=',',header=None)
df.columns=['id','fname','lname','age','pho','loc']
print(df)


print("*"*100)
df1=df.loc[df['age']==21] [['fname','lname','age','pho']]
print(df1)

print("*"*100)
df1=df.loc[df['age']>21] [['fname','lname','age']]
print(df1)

print("*"*100)
df1=df.loc[df['loc']=='Chennai'] [['fname','lname','age','pho']]
print(df1)


print("*"*100)
df1=df.loc[(df['loc']=='Chennai')&(df['age']>21)] [['fname','lname','age']]
print(df1)


print("*"*100)
df1=df.sort_values(by='age',ascending=False)
print(df1)


print("*"*100)
df1=df.sort_values(by='fname')
print(df1)


#maximum age,2 employes,fname,lname,age,pho
print("*"*100)
df1=df.sort_values(by='age',ascending=False) \
    [['fname','lname','age','pho']].head(2)
print(df1)


#minimum age ,1 employei,fname,lname,age
print("*"*100)
df1=df.sort_values(by='age') \
    [['fname','lname','age']].head(1)
print(df1)


#loc=chennai,maximum age,1 employeee,fname,lname,age
print("*"*100)
df1=df.loc[df['loc']=='Chennai'].sort_values(by='age',ascending=False) \
    [[ 'fname','lname','age']].head(1)
print(df1)
print("*"*100)


df1=df.groupby('loc') ['loc'].count() \
    .sort_values(ascending=False)
print(df1)

