a=open('test1.txt','r')
print (a.read())
a.close()
b=open('test1.txt','w')
b.write('this is abhi')
b.close()

c=open('test1.txt','a')
c.write('from salem')

c.close()
d=open('test2.txt','w')
d.write(c)
