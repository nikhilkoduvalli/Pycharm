f=open("C:/Users/nikhi/OneDrive/my/Desktop/pycham/customer1.txt","r")
for i in f:
    data=i.split(",")
    # proff=data[4]
    # if proff=="Doctor":
    #     print(data[1:5])
    age=data[3]
    if age>"50":
        print(data[1:4])