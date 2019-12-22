'''#if no arguments paased
def greet(name="bita"):
    print("hi"+name)
greet()'''

#pass by values
'''a=10
def change(b):
    print("old value",b)
    b=200
    print("new value",b)

change(a)
print(a)'''

#pass by reference
'''a=[1,2,3]
def change(b):
    print("old list",b)
    b[0]=20
    b[1]=30
    print("new list",b)
change(a)
print(a)'''

#adding list same as pass by value and pass by reference
'''list1=[1,2,3]
list2=list1
list1+=list2
#list1=list1+list2

print(list1)
print(list2)'''
#unpacking (the elements of list and value of dictionary) for the function
'''def unpack(a,b,c,d):
    print(a,b,c,d)
list1=[1,2,3,4]
dict1={"a":"red", "b":"pink", "c":"orange", "d":"green"}
unpack(*list1)
unpack(**dict1)'''
#global variable
'''a="hai"#global varaiable cant change by function
def fn():
    print(a)
fn()'''
#local variable
'''a="hai"
def fn():
    a="bye"#local variable can change by function
    print(a)
fn()
print(a)'''


