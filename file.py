#file handling programs
'''username=input("enter the name:")
password=input("enter the password")
newdict={'n':username,'p':password}
wte=open('newdoc.txt','a')
wte.write(newdict[n])
wte.write(newdict[p],'\n')
wte.close()
rad=open('newdoc.txt','r')
print(rad.read())
rad.close()'''

         
import json
username=input("enter the name")
password=input("enter the password")
dict1={username:password}
wte=open('newdoc.txt','a')
wte.write('{}\n'.format(dict1))

wte.close()
rad=open('newdoc.txt','r')
a=rad.read()
print(a)
print(a.find('school'))
#print(dict1['school'])
rad.close()



