from itertools import groupby

import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/OneDrive/my/Desktop/assignment/txn.txt',header=None)
df.columns=['oder_id','purchaced_date','customer_id','payment_amound','catugury','product','city','state','payment_way']
print(df)


#1
print('*'*100)
print(df.shape)


# 2. jan month oid,cusno,category,product,state
 # A. Row count
print("*"*100)
df2=df.loc[(df['purchaced_date']>='01-01-2011')&(df['purchaced_date']<='01-31-2011')] \
    [['oder_id','purchaced_date','customer_id','payment_amound','catugury','product','city','state','payment_way']]
print(df2.shape)

#3
# 3. July Month oid,cusno,category,product,state
#  B. Row count

print("*"*100)
df2=df.loc[(df['purchaced_date']>='07-01-2011')&(df['purchaced_date']<='07-31-2011')] \
    [['oder_id','purchaced_date','customer_id','payment_amound','catugury','product','city','state','payment_way']]
print(df2.shape)



#4
print('*'*100)
df4=df.groupby('catugury') ['catugury'].count() \
    .sort_values(ascending=False)
print(df4)


#5
print('*'*100)
df5=df.loc[df['catugury']=='Outdoor Recreation']
print(df5)


#6

print('*'*100)
df6=df.groupby('payment_way') ['payment_way'].count()
print(df6)


#7
print('*'*100)
df7=df.loc[(df['purchaced_date']>='01-01-2011')&(df['purchaced_date']<='07-01-2011')] \
    .groupby('purchaced_date') ['purchaced_date'].count()
print(df7)



#8
print('*'*100)
df8=df.groupby('catugury') ['payment_amound'].sum()
print(df8)


#9
print('*'*100)
df9=df.groupby('catugury') ['payment_amound'].max()
print(df9)


#10
print('*'*100)
df10=df.groupby('catugury') ['payment_amound'].mean()
print(df10)

#11
print('*'*100)
df11=df.groupby('payment_way') ['payment_amound'].sum()
print(df11)


#12
print('*'*100)
df12=df.loc[df['catugury']=='Indoor Games'].groupby('catugury') ['payment_amound'].sum()
print(df12)


#13
print('*'*100)
df13=df.groupby('state') ['state'].count()
print(df13)


