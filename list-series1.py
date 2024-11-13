import numpy as np
import pandas as pd
a=pd.Series([1,2,3,4,5,6,7,8])
print(a)
print(a.shape)
print(a.size)
print(a.dtype)


#head()   -get first n element as output(defoult it get first 5 elements as otput) -print(matrix.head(n))

print(a.head())


#tail()   --get last n element as output(defoult it get last 5 elements as otput)  -print(matrix.tail(n))


print(a.tail())
