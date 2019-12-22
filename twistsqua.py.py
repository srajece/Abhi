num=int(input("enter the number:"))
logic=((2*num)-1)
low=0
high=logic-1
squa=[[0 for i in range (logic)] for j in range (logic)]
#print(squa)
for i in range(0,num):
    #print(i)
    #print(num)

    for j in range(low,high+1):
        squa[low][j]=num
    
        
    for x in range(low+1,high+1):
        squa[x][high]=num
    

    for y in range(high-1,low-1,-1):
        squa[high][y]=num
    
    
    for z in range(high-1,low,-1):
        squa[z][low]=num
    num=num-1
    low=low+1
    high=high-1
    #print(num)

    
for row in range(0,logic):
    for colunm in range(0,logic):
        print(squa[row][colunm],end="\t")
    print()

