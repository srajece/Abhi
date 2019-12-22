#string manuplation
word=input("enter the word:").lower()
for i in word: 
    if i=="e" or i=="o" or i=="u" or i=="i" or i=="a":
        i=ord(i)+1
        neword=chr(i)
        print(neword,end='')
    else:
        print(i,end="")


#other method
'''word=input("enter the word:").upper()
case=ord("word")
for i in case:
    if i==69 or i==79 or i==85 or i==73:
        i=i+1
    elif i==65:
        i=90
    else:
        pass
    newword=chr(case)
    print(word)
    print(newword)'''
        

