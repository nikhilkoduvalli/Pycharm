line="cat rat cat rat bat bat rat cat rat cat"
dic={}
data=line.split(" ")
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

