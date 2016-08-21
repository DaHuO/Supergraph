filein=open("B-large.in")
fileout=open("B-large.out","w")
asdf=[]
for get in filein:
    asdf.append(get.rstrip('\n'))
a=int(asdf[0])
for x in range(1,a+1):
    b=asdf[x]
    count=0
    result=0
    q='-'
    for  z in b:
        if(z=='-'):
            count=count+1
            if(q=='+'):
                result=result+1
                q='-'
        else:
            if(count!=0):
                result=result+1
            count=0
            q='+'
    if(count!=0):
        result=result+1
    #result=str(result)
    zz=str(x)
    result=str(result)
    #print(result)
    fileout.write("Case #"+zz+": "+result+'\n')
filein.close()
fileout.close()
