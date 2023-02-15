a=int(input("enter your percentage"))
if(a>=0 and a<=100):
    if(a<=100 and a>=90):
        print(f"your passed with {a} A+ grade")
    elif(a<90 and a>=80):
        print(f"your passed with {a} A grade")    
    elif(a<80 and a>=70):
        print(f"your passed with {a} B+ grade")
    elif(a<70 and a>=60):
        print(f"your passed with {a} B grade")
    elif(a<60 and a>=50):
        print(f"your passed with {a} C+ grade")
    elif(a<50 and a>=40):
        print(f"your passed with {a} C grade")
    else:
        print("your are fail")
    
else:
    print("Plz enter the valid percentage")




print("Code is executed !!!")