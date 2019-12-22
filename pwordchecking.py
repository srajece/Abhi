#password checking program
secrete_password='abhi'
for i in range(0,3):
        pword=input("enter the password").lower()
        if pword==secrete_password:
            print("correct password")
            break
        else:
            print("incorrect password")
        if i ==2:
            print("timed out")
