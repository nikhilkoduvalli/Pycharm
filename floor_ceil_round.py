# floor---->used to discard the integer part and gives only the index
# ceil----->used to discard the integer part and gives the next highest number
# round---->if the integer value larger than 5 gives next highest value,less than 5 gives only the index value
            #if the integer is 5 it come from odd then return the same else even return highest






import numpy as np
a=np.array([[1.2,2.4,3.3,4.6],[5.1,6.2,7.5,8.4],[1.3,2.2,3.5,4.1],[2.5,6.1,7.4,2.1]])
print(a)
print("*"*100)
b=np.floor(a)
print(b)
print("*"*100)
c=np.ceil(a)
print(c)
print("*"*100)
d=np.round(a)
print(d)