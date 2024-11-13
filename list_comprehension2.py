# methode 2
# range of elements added to a list based on one condition
#
# syntax:
#
#        var=[print range if condition]

# lst=[i for i in range(1,21) if i%2==0]
# print(lst)


# lst=[i for i in range(1,31) if i%2==1]
# print(lst)

# lst=[i**2 for i in range(1,26) if i%5==0]
# print(lst)

lst=[i for i in range(1,51) if i%2==0 and i%5==0]
print(lst)