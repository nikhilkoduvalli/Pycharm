# method 3

# syntax:
#       var=[print1 if condition1 else print range()]
#       var=[print1 if condition1 else print2 if condition2 else print3 range()]





#
# lst=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,51)]
# print(lst)

#
# lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,30)]
# print(lst)


lst=[(i,"small") if i<=15 else (i,"medium") if 15<i<=35 else (i,"large") for i in range(1,51)]
print(lst)