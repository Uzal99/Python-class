# row=int(input("Enter the row value: "))
# col=int(input("Enter the col value: "))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("\n")
# print("close statement")
row=int(input("Enter the row value: "))
for i in range (1,row+1):
    for j in range(row,i-1,-1):
        print("*",end=" ")
    print("\n")
print("close statement")