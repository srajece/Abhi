z=["bita","academy","python","course"]
y=list(map(str.upper,z))
print(y)
'''
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
areas=list(map(round,circle_areas,[2 for i in range(6)]))
print(areas)'''
'''

items = [1, 2, 3, 4, 5]
sqr=list(map(lambda x:x*x,items))
print(sqr)'''
'''
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)'''
'''
number_list = range(-5, 5)

less_than_zero = list(map(lambda x: x < 0, number_list))
print(less_than_zero)'''
'''import time
list1 = [1, 2, 3, 4,5,6,7,8,9,7,5,5,4,8,6,2,1,8,12,5,8,5,5,56,8,6,4,9,6664,54]




from functools import reduce

start=(time.time())
product = reduce((lambda x, y: x * y), list1)
stop=time.time()
print('exe time: ',(stop-start))

start=(time.time())
product=1
for num in list1:
    product = product * num
    
stop=time.time()
print('exe time: ',(stop-start))'''
