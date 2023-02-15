# a=int(input("enter te number"))
# fact=1
# if(a==0):
#     print("factorial of 0 is 1")
# elif(a==1):
#     print("factorial of 1 is 1")
# else:
#     for i in range(1,a+1):
#         fact=fact*i
#     print(fact)
a=int(input("enter the number"))
fact=1
i=1
if(a==0):

    print("factorial of 0 is 1")
elif(a==1):
    print("factorial of 1 is 1")
else:
    while(i<=a):
        fact=fact*i
        i=i+1
    print(fact)
