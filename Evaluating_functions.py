# count
#  -each columnwise data

#newdf=olddf.groupby('colname') ['colname'].count()


import numpy as np
import pandas as pd

# id ,fname,lname,age,prof,salary

lst=[[101,"vinay","k",28,"Big data",15000],
     [102,"sarang","p",34,"python",22000],
     [103,"Sourav","g",64,"testing",44000],
     [104,"Sanjay","t",67,"Python",34000],
     [105,"Lokesh","T",54,"Python",25000],
     [106,"Suresh","M",34,"Python",34000],
     [107,"Ragesh","T",23,"DataScience",45000]]


df=pd.DataFrame(lst)
df.columns=["id","fname","lname","age","prof","salary"]
# print(df)

#-count sort by profession
df1=df.groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(df1)


#-count sort by age
df1=df.groupby('age') ['age'].count() \
    .sort_values(ascending=False)
print(df1)

