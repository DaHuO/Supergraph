filein=open("A-large.in")
fileout=open("A-large.out","w")
asdf=[]
for get in filein:
    asdf.append(get.rstrip('\n'))
a=int(asdf[0])
for main in range(1,a+1):
    num=int(asdf[main])
    zz=str(main)
    if(num==0):
        fileout.write("Case #"+zz+": "+"INSOMNIA\n")
    else:
        jkl=[]
        for j in range (0,10):
            jkl.insert(j,-1)
        for x in range (1,1000001):
            flag=0
            b=x*num
            b=str(b)
            for z in b:
                z=int(z)
                jkl.pop(z)
                jkl.insert(z,z)
            for i in range (0,10):
                if(jkl[i]==i):
                    flag=flag+1
            if(flag==10):
                bo=str(b)
                fileout.write("Case #"+zz+": "+bo+'\n')
                break
filein.close()
fileout.close()
