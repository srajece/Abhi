#file handling programs
import os
rad=open('test1.txt','r')
for line in rad:
    #print(line)
    indx=line.find('bita=')
    #print(indx)
    valinx=indx+5
    newline=line[valinx:]
    #print(newline)
    indx2=newline.find(" ")
    #print(indx2)
    nwinx=indx+indx2
    #print(nwinx)

    word=line[(indx+5):].split()[0]
    #print(word)
    newval=float(word)+50.5512
    #print(newval)
    newsen=line[:valinx]+str(newval)+newline[indx2:]
    print(newsen)
    #rad.close()
    wrt=open('test.txt','a')
    print(wrt.write(newsen))
    wrt.close()

rad.close()

os.remove()

