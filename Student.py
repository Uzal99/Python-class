math=int(input("enter your math no."))
science=int(input("enter your science no."))
computer=int(input("enter your computer no."))
english=int(input("enter your english no."))
if(100>=math>=0 and 100>=science>=0 and 100>=computer>=0 and 100>=english>=0):
    print("This is valid number")
    if(math>=40 and science>=40 and computer>=40 and english>=40):
        print("you are pass")
        total=math+science+computer+english
        per=(total/400)*100
        if(per<=100 and per>=90):
            print(f"your passed with {per} A+ grade")
        elif(per<90 and per>=80):
            print(f"your passed with {per} A grade")    
        elif(per<80 and per>=70):
            print(f"your passed with {per} B+ grade")
        elif(per<70 and per>=60):
            print(f"your passed with {per} B grade")
        elif(per<60 and per>=50):
            print(f"your passed with {per} C+ grade")
        elif(per<50 and per>=40):
            print(f"your passed with {per} C grade")
    else:
        print("you are fail")


else:
    print("Invalid number")

    
