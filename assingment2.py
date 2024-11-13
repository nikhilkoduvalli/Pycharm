import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/assignment/movies_cleaned_pandas.txt',sep=",",header=None)
df.columns=['movie_id','mname','year','rating','duration']
print(df)


#1
print('*'*100)
print(df.shape)
print('*'*100)


#2
df2=df.drop_duplicates()
print(df2.shape)
print('*'*100)


#3
df3=df.sort_values(by='year',ascending=False)
print(df3)
print('*'*100)

#4
df4=df.sort_values(by='rating',ascending=False) \
    [['mname','year','rating']].head(5)
print(df4)

#5
print('*'*100)
df5=df.sort_values(by='rating') \
    [['mname','year','rating']].head(3)
print(df5)

#6
print('*'*100)
df6=df.groupby('year') ['mname'].count() \
    .sort_values(ascending=False)
print(df6)

#7
print('*'*100)
df7=df.groupby('rating') ['rating'].count()
print(df7)

#8
print('*'*100)
df8=df.loc[(df['year']==2008)&(df['rating']>3)]
print(df8.shape)

#9
print('*'*100)
df9=df.sort_values(by='duration',ascending=False) \
    [['mname','year','rating','duration']].head(1)
print(df9)

#10
print('*'*100)
df10=df.sort_values(by='rating') \
    [['mname','year','rating','duration']].head(1)
print(df10)

#11
print('*'*100)
df11=df.loc[(df['rating']>4)&(df['year']>2005)]
print(df11)
print('*'*100)
df11a=df11.sort_values(by='rating',ascending=False) \
    .head(1)
print(df11a)
print('*'*100)
df11b=df11.sort_values(by='rating') \
    .head(1)
print(df11b)



# 12. 2008 movies count
print('*'*100)
df12=df.loc[df['year']==2008].groupby('year') ['year'] \
    .count()
print(df12)

#13. 1975-2000 movies collect
#     A. Row count
print('*'*100)
df13=df.loc[(df['year']>=1975)&(df['year']<=2000)]
print(df13.shape)


#14.
print('*'*100)
df14=df.loc[(df['year']>=1975)&(df['year']<=2000)&(df['rating']>3.5)]
print(df14.shape)











