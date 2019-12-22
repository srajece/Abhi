#dictionary related program
'''
phonedic={2:"abc",3:"def"}
number=int(input("enter the number:"))
clik=int (input("number of click:"))
if clik%3==1:
    clik=0
elif clik%3==2:
    clik=1
elif clik%3==0:
    clik=2
print(phonedic[number][clik])'''
#other method    
while True:
    phonedic={2:"cab",3:"fde",4:"ihg",5:"ljk",6:"onm",7:"srqp",8:"vut",9:"zyxw"}
    number=int(input("enter the number:"))
    clik=int (input("number of click:"))
    if (number==7) or (number==9):
        print(phonedic[number][clik%4])
    else:
        print(phonedic[number][clik%3])
