import numpy as np
import pandas as pd
df=pd.read_csv("/Users/nikhi/Downloads/movies.csv",sep=',',header=None)
df.columns=['id','moviename','year','rating','duration']
print(df)
