# string="luminar technolab"
# lst=[i for i in string if i in "aeiouAEIOU"]
# print(len(lst))




string="luminar technolab"
lst=[i for i in string if i not in "aeiouAEIOU"]
print(len(lst))