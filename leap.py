#to check leap year or not
while True:
    year=int(input("enter the year:"))
    if year%4==0:
        if year%100!=0:
            print("this is a leap year")
        else:
            if year%400==0:
                print("this is leap year")
            else:
                print("this is not leap year")
    else:
        print("this is not leap year")
            
               

