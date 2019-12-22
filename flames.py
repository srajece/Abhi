'''name1=input("enter the first name")
list1=list(name1)
name2=input("enter the second name")
list2=list(name2)
count=0
#dict2={"f":"friends","l":"lovers","a":"affection","m":"marriage","e":"enemy","s":"sisters"}
if len(list1)<len(list2):
    for ele in range(0,len(list1)):
            if list1[ele] not in list2:            
                count=count+1
            
            elif list1[ele] in list2:
                list2.remove(list1[ele])
    print(count+len(list2))
elif len(list1)>len(list2):
    for ele in range(0,len(list2)):
        if list2[ele] not in list1
            count=count+1
        elif list2[ele] in list1:
            list1.remove(list2[ele])
    print(count+len(list1))'''

div=16
game=['f','l','a','m','e','s']
count=4
while count!=0:
    num=div%count
    print(num)
    game.pop(num-1)
    print(game)
    count=count-1
    newgame=game[num-1:num+1]+game[0:num-1]
print(newgame)


            

