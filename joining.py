# import numpy as np
# a=np.array([6,8,1,2,3,4,6,7,8,9,10,15])
# b=np.array([1,2,3,4])
# c=np.concatenate((a,b))
# print(c)


import numpy as np
a=np.array([[1,2,3],[5,6,7]])
b=np.array([[1,2,3],[4,5,6]])
c=np.concatenate((a,b),axis=1)
print(c)