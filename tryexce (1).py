#try except finnaly concept
'''a=[1,2,3,4]
try:
    print(b)
except IndexError:
          print("hi")
finally:
          print(a[0])'''

"""#bracket checking

input1="(({[]}))"
if len(input1)%2!=0:
    print("invalid")
else:
    count1=len(input1)
    for i in range(0,len(input1)):
        
        if input1[i]="("and==input1[count1-1]=")":
            print(input1[i],input1[count1-1])
            count1-=1
            print("equal brackets")
    else:
        print("unequal brackets")"""

#eval concept

str1="1plus5minus8div2mul2"
str2=str1.replace("plus","+").replace("minus","-").replace("div","/").replace("mul","*")
print(str2)
print(eval(str2))
    
