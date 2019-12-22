#simple program to understand the flag concept
valid=True
while True:
    a=input("enter the word:")
    for i in a:
        if i!="b":
            valid1=False
        else:
            valid1=True
            
            break
    if not a.isalpha():
        valid2=False
    else:
        valid2=True
    valid=valid1 and valid2
        
    if valid:
        print("valid word")
    else:
        print("invalid word")
