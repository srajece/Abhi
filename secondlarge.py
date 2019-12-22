newlist=[45,67,89,23,12,45,67,90]

for j in range(0,2):
    maxi=newlist[0]
    for i in range(0,len(newlist)):
        if newlist[i]>maxi:
            maxi=newlist[i]
    
    newlist.remove(maxi)
    print(newlist)
    print("the maximum",maxi)
'''for j in range(0,len(newlist)):
    if newlist[j]>maxii:
        maxii=newlist[j]
print("the second maximum is",maxii)'''


    
                     
                     
    
        

        
        
