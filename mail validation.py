#mail validation programe
'''valid=True
while True:
    mail_id=input("Enter the mail_ID:").lower()

    l=len(mail_id)
    if mail_id.count("@")>1:
        valid=False
    for i in mail_id:
         if i=="@":
            a=mail_id.index("@")
    
    if mail_id[a-1]==".":
        valid=False
    for i in range(a+1,a+4):
        
        if not mail_id[i].isalpha():
            valid=False

    for i in range(a+1,len(mail_id)):
        
    
        if mail_id[i]==".":
            d=i
            
    if not mail_id[d+1].isalpha():
        valid=False

    if valid:
        print('email is valid')
    else:
        print('email is invalid')'''


'''# my own try to understand the concept of flag
mail_id="abhi@gmail.com"
for i in range(0,len(mail_id)):
    if i=="@":
        valid=True
    else:
        valid=False
if valid:
    print('email is invalid')
else:
    print('email is valid')''''

        
'''if a-1 ==".":
    print("invalid mail_id")
else:
    print("valid mail.id")
if d>a:
    print("valid mail_id")
else:
    print("invalid mail_id")
for i in range(d,d+2):
    if not mail_id[i].alpha():
        print("invalid mail_id")
    else:
        print("valid mail_id")'''
