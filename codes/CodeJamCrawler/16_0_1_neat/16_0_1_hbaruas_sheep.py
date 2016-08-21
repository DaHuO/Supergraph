fileinput=open("A-large.in")
fileoutput=open("A-large.out","w")
pqrs=[]
for get in fileinput:
    pqrs.append(get.rstrip('\n'))
a=int(pqrs[0])
for main in range(1,a+1):
    number=int(pqrs[main])
    ss=str(main)
    if(number==0):
        fileoutput.write("Case #"+ss+": "+"INSOMNIA\n")
    else:
        jkl=[]
        for j in range (0,10):
            jkl.insert(j,-1)
        for x in range (1,1000001):
            counter=0
            b=x*number
            b=str(b)
            for z in b:
                z=int(z)
                jkl.pop(z)
                jkl.insert(z,z)
            for i in range (0,10):
                if(jkl[i]==i):
                    counter=counter+1
            if(counter==10):
                bo=str(b)
                fileoutput.write("Case #"+ss+": "+bo+'\n')
                break
fileinput.close()
fileoutput.close()
