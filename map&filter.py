# list1=[1,2,3,4,5]
# list2=[i**2  for i in list1]
# list3=[i for i in list1 if i%2==0]
# print(list2)
# print(list3)



# lst=[1,2,3,4,5,6,7,8,9,10]
# f=list(map(lambda num:num**2,lst))
# print(f)



# lst=[1,2,3,4,5,6,7,8,9,10]
# f=list(filter(lambda num:num%2==0,lst))
# print(f)



lst=[10,11,12,13,14,15,16,17,18,19,20]
f=list(filter(lambda num:num%2==1,lst))
s=list(map(lambda num:num**2,f))
print(s)

