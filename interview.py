# lst=[12,8,20,15,3,6,3,8]
# c=sum(lst)
# lst2=[]
# for i in lst:
#     d=c-i
#     lst2.append(d)
# print(lst2)

#[1,8,4,9,6,20]
lst = [1, 3, 6, 8, 6, 5, 4, 7, 9, 11, 13, 9, 7, 6, 8, 12, 13, 15, 20, 17, 15]
fi_lst = []

for i in range(1, len(lst) - 1):
    if (lst[i] - 1 > lst[i - 1] and lst[i] - 1 > lst[i + 1]) or (lst[i] + 1 < lst[i - 1] and lst[i] + 1 < lst[i + 1]):
        fi_lst.append(lst[i])

print(fi_lst)


