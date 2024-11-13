import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df)


print(df.isna().sum())
df1=df.fillna('india')
print(df1.isna().sum())
print("*"*100)

#1
print(df1.shape)
print("*"*100)


#2
df2=df1.drop_duplicates()
print(df2.shape)
print("*"*100)


#3
df3=df1.sort_values(by='age',ascending=False) \
    [['fname','lname','prof','loc']].head(10)
print(df3)
print("*"*100)

#4
df4=df1.sort_values(by='age') \
    [['fname','lname','prof','loc']].head(5)
print(df4)
print("*"*100)

#5
df5=df1.groupby('loc') ['loc'].count() \
    .sort_values(ascending=False)
print(df5)
print("*"*100)

#6
df6=df1.loc[df1['loc']=='australia']
print(df6)
print("*"*100)

#7
df7=df1.groupby('age') ['age'].count() \
    .sort_values(ascending=False)
print(df7)
print("*"*100)

#8
df8=df1.groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(df8)
print("*"*100)
print("*"*100)


df9=df1.loc[df1['loc']=='india']
print(df9)
print("*"*100)

#9a
print(df9.shape)
print("*"*100)

#9b
df9b=df.groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(df9b)
print("*"*100)


#9c
df9c=df9.sort_values(by='age',ascending=False) \
    [['fname','lname','age','prof']].head(3)
print(df9c)
print("*"*100)

#9d
df9d=df9.sort_values(by='age') \
    [['fname','lname','age','prof']].head(3)
print(df9d)
print("*"*100)

#9e
df9e=df9.loc[df9['age']>40]
print(df9e)
print("*"*100)

#9f
df9f=df9.loc[(df9['age']>=30)&(df9['age']<=40)] \
    .groupby('prof') ['prof'].count()
print(df9f)
print("*"*100)


df10=df1.loc[df1['loc']=='us']
print(df10)
print("*"*100)

#10a
print(df10.shape)
print("*"*100)


#10b
df10b=df10.groupby('age') ['age'].count()
print(df10b)
print("*"*100)


#10c
df10c=df10.groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(df10c)
print("*"*100)


#10d
df10d=df10.loc[(df10['prof']=='Civil engineer')&(df10['age']>30)]
print(df10d)
































