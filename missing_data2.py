import numpy as np
import pandas as pd
df=pd.read_csv('/Users/nikhi/Downloads/missing_data.csv',sep=',')
print(df)


# print(df.isna().sum())
#
#
# df.fillna(350,inplace=True)
# print(df)



#how to fill missing value using specific coloumn

# df['Calories'].fillna(400,inplace=True)
# print(df)
# print(df.isna().sum())

# df.fillna({'Calories':400},inplace=True)
# # print(df)
# df.fillna({'Date':'2024/09/30'},inplace=True)
# print(df)
# print(df.isna().sum( ))

#filling by mean

# x=df['Calories'].mean()
# print(x)
#
# df.fillna({'Calories':x},inplace=True)
# print(df.isna().sum())



#filling by mode()

#
# x=df['Calories'].mode()[0]
# print(x)
#
# df.fillna({'Calories':x},inplace=True)
# print(df.isna().sum())
#
#
#
# d=df['Date'].mode()[0]
# df.fillna({'Date':d},inplace=True)
# print(df.isna().sum())


# print(df.isna().sum())
#
# #to drop all the lines having missing value
# df.dropna(inplace=True,ignore_index=True)
#
# print(df)


#to drop a row that based on a petrticular column that having missing value

#
# df.dropna(subset=['Calories'],inplace=True,ignore_index=True)
# print(df)




#how to handle wrong data

#-----wrong datas are the datas that not possible on a current set of data ,it separate from the


# x=df['Duration'].mode()[0]
# df.loc[7,'Duration']=x
# print(df)


x=df['Calories'].mean()
for i in df.index:
    if df.loc[i,'Calories']>400:
        df.loc[i,'Calories']=x
print(df)


