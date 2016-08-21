fileinput=open("B-large.in")
fileoutput=open("B-large.out","w")
sfgh=[]
for bet in fileinput:
    sfgh.append(bet.rstrip('\n'))
a=int(sfgh[0])
for x in range(1,a+1):
    b=sfgh[x]
    count123=0
    result123=0
    q='-'
    for  z in b:
        if(z=='-'):
            count123=count123+1
            if(q=='+'):
                result123=result123+1
                q='-'
        else:
            if(count123!=0):
                result123=result123+1
            count123=0
            q='+'
    if(count123!=0):
        result123=result123+1
   
    qq=str(x)
    result123=str(result123)
    
    fileoutput.write("Case #"+qq+": "+result123+'\n')
fileinput.close()
fileoutput.close()
