#printpattern
'''num=5
count=1
for i in range(0,num):
    print(count,end="")
    count=count+1
    print()
for j in range(0,num):
    print(count,end="")
    count=count+1'''
    

#printpattern(correct pattern)    
'''num=5

for i in range(1,num+1):
    count=1
    for j in range(1,i+1):
        print(i,end="\t")
        i=i+(num-count)
        count+=1
    print()'''
        
    

#printpattern
num=5
dis=15

for i in range(1,num+1):
    count=1
    for j in range(1,i+1):
        print(dis,end="\t")
        dis=dis-(num-count)
        count=count+1
    print()
    
