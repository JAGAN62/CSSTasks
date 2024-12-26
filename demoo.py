list=[3,7,2,1,9,0,2,8]

# for i in range(len(list)):
#     for j in range(len(list) - i - 1):
#         if list[j] > list[j + 1]:
#             list[j], list[j + 1] = list[j + 1], list[j]

# print(list)


for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i] #temp=list[i];list[i]=list[j];list[j]=temp
print(list)