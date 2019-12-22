#to find the user name
'''a="abhi@gmail.com"
c=""
for i in a:
    if i=="@":
        break
    else:
        print(i,end="")'''
    

    
#to split
'''a="bita academy"

print(a.split(" "))'''

#to join
'''a=["a","b","c"]
c='test'
b=c.join(a)
print(b)'''

#to convert string to int
'''a="1 2 3 4 5"
b=a.split(" ")
print(b)
for i in range(0,len(b)):
    b[i]=int(b[i])
print(b)'''
#other methods for two changing paramaters
'''index=o
for i in b:
    b[index]=int(i)
    index=index+1'''
#while loop
'''a=0
while a<10:
    a=a+1
    if(a!=5):
        print(a)
    else:
        pass'''
# to find &replace
'''a="bita abhi academy bita"
b=a.find("bita")
print(b)
c=a.replace("bita","study")
print(c)'''
#car program
started=False
while True:
    action=input("enter the command:").lower()
    
    if action=="start":
        if not started:
            print("car is going to be started")
            started=True
        else:
            print("the car is already started")
    elif action=="stop":
        if started:
            print("car is  going to be stopped")
            started=False
        else:
            print("car is already stopped")
    elif action=="help":
        print("type start to start\n","type stop to stop\n", "type help to help\n menu")
    elif action=="exit":
        break
    else:
        print("i dont understand")
    
    

