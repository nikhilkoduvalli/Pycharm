#Arg sorthing

#1Diamension



#
# import numpy as np
# a=np.array([1,2,5,0,5,7,3,7,5,9])
# print(a)
# print("*"*100)
# b=np.argsort(a)  #it will gives the output of the index value of the sorted list elements
# print(b)
# print("*"*100)
# c=np.argmax(a)  #return the index of the largest element in the array
# print(c)


#2Diamension
#
import numpy as np
a=np.array([[1,2,3,4],[6,8,3,7],[3,0,6,4],[5,8,2,0]])
print(a)
print("*"*100)

b=np.argsort(a)            #it will gives the output of the index value of the sorted list elements
print(b)
print("*"*100)
c=np.argsort(a,axis=0)     #it will gives the output of the index value of the sorted list elements in column wise
print(c)
print("*"*100)
e=np.argmax(a,axis=1)  #return the index of the largest element in the array
print(e)
print("*"*100)
f=np.argmax(a,axis=0)  #return the index of the largest element in the array
print(f)
print("*"*100)
g=np.argmax(a)
print(g)
print("*"*100)
h=np.argmin(a,axis=1)  #return the index of the largest element in the array
print(h)
print("*"*100)
i=np.argmin(a,axis=0)  #return the index of the largest element in the array
print(i)
print("*"*100)
j=np.argmin(a)
print(j)


