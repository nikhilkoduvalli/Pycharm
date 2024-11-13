# import numpy as np
# a=np.array([5,8,1,9,10,4,7,9,3,9,18,40,5])
# b=a>10
# c=a[b]
# print(c)


import numpy as np
a=np.arange(1,51)
b=a%5==0
c=a[b]
print(c)