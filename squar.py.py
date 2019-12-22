num=int(input("enter the number:"))
count=1
low=0
high=num-1
squa=[[0 for i in range(num)] for j in range (num)]
for i in range(0,int((num+1)/2)):
    #print(i)
    #print(count)
    for j in range(low,high+1):
        squa[low][j]=count
        count=count+1
        
    for x in range(low+1,high+1):
        squa[x][high]=count
        count=count+1
        
    for y in range(high-1,low-1,-1):
        squa[high][y]=count
        count=count+1
    
    for z in range(high-1,low,-1):
        squa[z][low]=count
        count=count+1
    low=low+1
    high=high-1
   
for row in range(0,num):
    for colunm in range(0,num):
        print(squa[row][colunm],end="\t")
    print()
print(squa)

        
    
    
