import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df)


# print("*"*100)
# df1=df[['fname','lname','age','prof']].head(25)
# print(df1)
# print("*"*100)
# df2=df[['fname','lname','age',]].tail(10)
# print(df2)
# print("*"*100)
#
#
#
# #to calculate the total number of missing value
# print(df.isna().sum())
# print("*"*100)
#
#
#
# #to fill the possition of the missing value
#
# df3=df.fillna('india')
# print(df3.isna().sum())
#
#
#
# print("*"*100)
# df1=df.iloc[5:11]
# print(df1)
#
# print("*"*100)
# df4=df.iloc[5:11,1:5]
# print(df4)
#
# print("*"*100)
# df5=df.iloc[1:31,1:]
# print(df5)
#
#
# print("*"*100)
# x=df.iloc[:,:-1]  #all rows exsept last coliumn
# print(x)
#
#
# print("*"*100)
# y=df.iloc[:,-1]   #all rows only last coloumn
# print(y)
#
#
# print("*"*100)
# dfc=df.loc[df['age']>50]    #costemer data that have age above50
# print(dfc)
#
#
#
# print("*"*100)
# df1=df.loc[df['age']>60] [['fname','lname','age','prof']]   #custemer details of fname,lname,age,prof that age >60
# print(df1)
#
#
# print("*"*100)
# df1=df.loc[df['loc']=='india'] [['fname','lname','age','prof']]  #list of indian custemer
# print(df1)
#
# print("*"*100)
# df1=df.loc[(df['loc']=='india')&(df['age']>50)] \
#     [['fname','lname','age','prof']]
# print(df1)
#
#



print(df.isna().sum())
df1=df.fillna('india')
print(df1.isna().sum())
print("*"*100)



df2=df.loc[df['loc']=='india'] [['fname','lname','age','prof']]
print(df2)
print("*"*100)


df3=df.sort_values(by='age',ascending=False) \
    [['fname','lname','age','prof']].head(5)
print(df3)

print("*"*100)


df4=df.sort_values(by='age') \
    [['fname','lname','age','prof']].head(3)
print(df4)
print("*"*100)


df5=df.loc[df['loc']=='uk'] [['fname','lname','age','prof']]
print(df5)
print("*"*100)


df6=df.loc[(df['age']>40)&(df['age']<60)] \
    [['fname','lname','age','prof']]
print(df6)
print("*"*100)


df7=df.loc[df['loc']=='india'].sort_values(by='age',ascending=False) \
    [['fname','lname','age','prof']].head(2)
print(df7)

print("*"*100)



df8=df.loc[(df['loc']=='india')&(df['prof']=='Doctor')] \
    [['fname','lname','age']]
print(df8)
print("*"*100)


df9=df.loc[df['prof']=='Pilot'].sort_values(by='age') \
    [['fname','lname','age']].head(1)
print(df9)
print("*"*100)


df10=df.loc[df['prof']=='Actor'].sort_values(by='age',ascending=False) \
    [['fname','lname','age']].head(1)
print(df10)



print("*"*100)
df1=df.loc[df['loc']=='india'].groupby('prof') \
    ['prof'].count() \
    .sort_values(ascending=False)
print(df1)

print("*"*100)
df1=df.loc[(df['loc']=='uk')&(df['age']>50)].groupby('age') \
    ['age'].count() \
    .sort_values(ascending=False)
print(df1)




