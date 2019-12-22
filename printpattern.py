#print pattern1
'''num=5
for i in range(1,num+1):
    print("*"*i)'''
#print pattern2
'''num=5
for i in range(num,0,-1):
    print("*"*i)'''
#print pattern3
'''num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end="")
    print("\r")'''
#print pattern4
'''num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''
#print pattern5
'''num=5
count=0
for i in range(0,num+1):
    for j in range(0,i+1):
        count=count+1
        print(count,end=" ")
    print()'''
#print pattern6
'''num=5
count=0
var=1
for i in range(0,num):
    for j in range(0,var):
        count=count+1
        print(count,end="\t")
    var=var+2
    print()'''
#print pattern7
'''num=5
for i in range(1,num+1):
    for j in range(1,(num-i)+1):
        print(" ",end="")
    for n in range(1,i+1):
        print("* ",end="")
    print()'''
#print pattern8
'''num=5
for i in range(1,num+1):
    for j in range(1,(num-i)+1):
        print(" ",end="")
    for n in range(0,2*i-1):
        print("*",end="")
    print()'''
  /. ././S.?f0ki'/k#print pattern9
num=6
for i in range(1,num+1):
    print("*"*i)
for j in range(num-1,0,-1):
    print("*"*j)
#print pattern10
'''num=6
for i in range(1,num+1):
    for j in range(num+1-i,1,-1):
        print(" ",end="")
    for n in range(1,i+1):
        print("*",end="")
    print()
for l in range(1,num+1):
    for m in range(1,l+1):
        print(" ",end="")
    for p in range(num-l+1,1,-1):
        print("*",end="")        
    print()'''
#print pattern11
'''num=5
for i in range(1,num+1):
    for j in range(num+1-i,1,-1):
        print(" ",end="")
    for n in range(1,i+1):
        print("* ",end="")
    print()
for k in range(1,num+1):
    for l in range(1,k+1):
        print(" ",end="")
    for m in range(num+1-k,1,-1):
        print("* ",end="")
    print()'''
#print pattern12
'''num=5
for i in range(1,num+1):
    count=i
    for j in range(num+1-i,1,-1):
        print(" ",end="")
    for n in range(1,i+1):
        print(count,end="")
        count=count-1
    for l in range(2,i+1):
        print(l,end="")
    print()'''
#print pattern13
'''num=5
for i in range(1,num+1):
    count=5
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(num+1-i,0,-1):
        print(count,end="")
        count=count-1
    print()'''
