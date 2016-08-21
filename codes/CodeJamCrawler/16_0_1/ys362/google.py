
f = open(r"C:\Users\ys362\Desktop\A-large.in",'r')
li = f.readlines()
T=int(li[0])
fw=open(r"C:\Users\ys362\Desktop\result-large.txt",'w')
for z in range(T):
    bar={}
    x=z+1  
    value=int(li[x])
    mvalue=value
    if value==0:
    	fw.write( "Case #{}: INSOMNIA\n".format(x))
    else:
        base = 1
        while len(bar) != 10:
        	mvalue=value*base
        	toString=str(mvalue)
        	for y in toString:
        	    bar[int(y)]=1
        	base+=1
        fw.write("Case #{}: {}\n".format(x,mvalue))