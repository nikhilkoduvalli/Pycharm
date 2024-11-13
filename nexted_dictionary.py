#id,fname,lname,age
#id,prof,salary,location





import numpy as np
import pandas as pd
dic={'id':[1,2,3,4,5],
     'fname':['Nandu','Nikhi','ashvin','layna','vyshnav'],
     'lname':['T','K','K','T','C'],
     'age':[21,20,21,27,25]}
df=pd.DataFrame(dic)
print(df)

dic1 ={'id':[3,4,5,6,7],
     'prof':['web developer','Data engineer','Data analist','Tester','Data analyst'],
     'salary':[25000,70000,50000,25000,50000],
     'loc':['knr','tvm','ern','knr','knr']}
df1=pd.DataFrame(dic1)
print(df1)
df3=pd.merge(df,df1,on='id',how='inner')
print(df3)
df4=df3.loc[df3['age']>20] [['id','fname','lname','age']]
print(df4)



df5=pd.merge(df,df1,on='id',how='left')
print(df5)



df6=pd.merge(df,df1,on='id',how='right')
print(df6)



df7=pd.merge(df,df1,on='id',how='outer')
print(df7)