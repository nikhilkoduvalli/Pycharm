import numpy as np
# a=np.array([[1,2,3,4],[6,8,3,7],[3,0,6,4],[5,8,2,0]])
# print(a)
# b=np.sort(a)
# print(b)
# c=np.sum(a,axis=0)
# print(c)


#axis

#axis=0   colomns
#axis=1   rows


a=np.array([[1,2,3,4],[6,8,3,7],[3,0,6,4],[5,8,2,0]])
print(a)
print("*"*100)
c=np.sum(a,axis=0)
print(c)
print("*"*100)
d=np.sum(a,axis=1)
print(d)
print("*"*100)
e=np.sort(a,axis=0)
print(e)
print("*"*100)
f=np.max(a)
print(f)
print("*"*100)
g=np.max(a,axis=0)
print(g)
print("*"*100)
l=np.max(a,axis=0)
print(l)
print("*"*100)
h=np.max(a,axis=1)
print(h)
print("*"*100)
i=np.min(a,axis=0)
print(i)
print("*"*100)
j=np.min(a,axis=1)
print(j)
print("*"*100)
k=np.min(a)
print(k)
