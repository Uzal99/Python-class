# row=int(input("Enter the row value: "))
# #col=int(input("Enter the col value: "))
# for i in range(1,row+1):
#     for j in range(row,i-1,-1):
#         print(j,end=" ")
#     print("\n")
# print("close statement")
num=int(input("Enter the row value: "))
for i in range (num):
    for j in range (i):
        print("*",end=" ")
    for k in range(num,i,-1):
        print(k,end=" ")
    print("\n")
print("close statement")