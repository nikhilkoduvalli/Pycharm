import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/assignment/heart.txt')
print(df)

print('*'*100)
print(df.shape)


print('*'*100)
print(df.dtypes)


print('*'*100)
x=df.iloc[:,:-1]
print(x)

print('*'*100)
y=df.iloc[:,-1]
print(y)




print('*'*100)
print(df.isna().sum())


#to calculate the unique values of a column

print(df['trestbps'].unique())
print('*'*100)
print(df['restecg'].unique())
print('*'*100)
print(df['thalach'].unique())
print('*'*100)
print(df['ca'].unique())
print('*'*100)
print(df['thal'].unique())
print('*'*100)






x=df['trestbps'].mean()
y=df['restecg'].mode()[0]
z=df['thalach'].mean()
w=df['ca'].mode()[0]
a=df['thal'].mode()[0]



df.fillna({'trestbps':x},inplace=True)
df.fillna({'restecg':y},inplace=True)
df.fillna({'thalach':z},inplace=True)
df.fillna({'ca':w},inplace=True)
df.fillna({'thal':a},inplace=True)
print(df.isna().sum())


print('*'*100)
x=df['chol'].mean()
for i in df.chol:
    if df.loc[i,'chol']>300:
        df.loc[i,'chol']=x

print(df)

