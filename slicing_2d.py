#2D array slicing

# syntax:
#         print(matrix[row index,coloumn index])








import numpy as np
a=np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]])
print(a)
print("*"*100)
print(a[1:,:3])         #row=1,2,3    coloumn=0,1,2
print("*"*100)
print(a[:2,1:4])        #row=0,1    coloumn=1,2,3
print("*"*100)
print(a[1:3,1::2])      #row=1,2    coloumn=1,3
print("*"*100)
print(a[::2,:4:2])      #row=0,2    coloumn=0,2
print("*"*100)
print(a[2:,::2])        #row=2,3    coloumn=0,2,4
print("*"*100)
print(a[0,:])           # print only 0th row
print("*"*100)
print(a[:,0])           #print only 0th column
