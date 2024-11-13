#identity matrix


#[1 0]
#[0 1]



#[1 0 0]
#[0 1 0]
#[0 0 1]

import numpy as np
a=np.identity(3,dtype=int)
b=np.eye(4,dtype=int)
print(a)
print("*"*100)
print(b)