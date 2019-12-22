#how to get input from shell
'''
name=input('enter your name: ')
print(name+"abhi")
print("welcome")'''

'''
#addition and type casting
num1=int(input('enter n1'))
print(type(num1))
num2=int(input('enter n2'))
c=str(num1+num2)
print("the sum of thwo numbers"+c)'''
#IF AND FOR AND WHILE
'''for i in "BITA":
    print(i)'''

'''for i in [1,2,3,4]:
    print(i)'''
'''#increment'''

'''for i in range(5):
    print(i)'''
#range (start,end,slicing) default start vale 0, slicing value 1
'''from sys import argv
for i in range(2,20,2):
    print(i)
    print(argv)'''
    

# range dont know it prints* infinitive
'''count=0
while(count<5):
    print('*')'''
#range know
'''count=1
while(count<=5):
    print("*"*count)
    count+=1'''

'''for i in range(1,5):
    print("a"*i)'''
#string methods
'''a="python batch"
print(a[0:6:2])
print(len(a))'''
#reverse index
'''a=" python"
print(a[-1])
print(a[-1:-4])'''
#reverse the string
'''a=" python fresh start"
print(a[-1])
print(a[-1:8:-1])'''
# to count the string
'''count=0
a="python"
for i in a:
    count=count+1
print("numbers of letters",count)'''
#to find divisible numbers by 3
'''a=[]
for i in range(1,100):
    
    if i%3==0:
        a.append(i)
print(a)
finalsum=0
for i in a:
    finalsum=finalsum+i
print(finalsum)'''
    


           
