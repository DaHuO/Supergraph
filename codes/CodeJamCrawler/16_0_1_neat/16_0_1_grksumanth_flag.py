fp=open('A-large.in','r')
fla='0'
val=0
def coun(k):
    count=1
    #print k
    global val
    if k=='0':
        val+=1
        print "Case #%s: INSOMNIA"%(val)
        return
    flag=[0,0,0,0,0,0,0,0,0,0,0]
    for y in k:
        y=int(y)
        if y==0:
            flag[0]=1
        elif y:
            flag[y]=1
    #print flag
    if sum(flag)<10:
        coune(k,flag,count)

def coune(k,flag,count):
    global val
    #print "counee called"
    count+=1
    #print count,"count"
    x=int(k)*count
    x=str(x)
    #print x
    for y in x:
        y=int(y)
        if y==0:
            flag[0]=1
        elif y:
            flag[y]=1
     #print flag
    if sum(flag)<10:
         coune(k,flag,count)
    else:
        val+=1
        print "Case #%s: %s"%(val,x)
for x in fp:
    if fla=='0':
        fla='1'
        pass
    else:
        coun(x.strip())
