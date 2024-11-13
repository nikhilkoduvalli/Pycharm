f = open('/Users/nikhi/OneDrive/my/Desktop/assignment/temper', 'r')
dic = {}
for i in f:
    data = i.rstrip("\n").split(',')
    district = data[0]
    temperature = int(data[1])

    if district in dic:
        if temperature > dic[district]:
            dic[district] = temperature
    else:
        dic[district] = temperature
f.close()
print(dic)