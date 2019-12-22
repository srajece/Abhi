#try except finnaly concept
'''a=[1,2,3,4]
try:
    print(b)
except IndexError:
          print("hi")
finally:
          print(a[0])'''

#bracket checking

input1="}{]["
brackets=["(",")","[","]","{","}"]
count=-1
if len(input1)%2!=0:
    print("invalid")
else:
    for i in range(0,int(len(input1)/2)):
        if input1[i] in brackets:
            ind=brackets.index(input1[i])
            #print(ind)
            try:
                if brackets[ind+1]==input1[count]:
                    count=count-1
                    if i==int(len(input1)/2)-1:
                        print("valid")
                else:
                    print("invalid")
                    break
            except IndexError:
                print("invalid")
                break
        
             

'''#eval concept

str1="1plus5minus8div2mul2"
str2=str1.replace("plus","+").replace("minus","-").replace("div","/").replace("mul","*")
print(str2)
print(eval(str2))'''
    
