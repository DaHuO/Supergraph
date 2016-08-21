


def get_div(n):
    if n>2 and n%2==0:
        return 2
    i=3
    while True:
        if (i*i>n or i>500):
            return -1
        if (n%i==0):
            return i
        i=i+2
        

def getBaseVal(base,len,interval):
    rv = base**(len-1)
    rv=rv+1
    db = base
    while(interval>0):
        if interval%2==1:
            rv=rv+db
        db=db*base
        interval=interval/2
    return rv
T = int(raw_input())
linija = raw_input().split()
N=int(linija[0])
J=int(linija[1])
#print J,N


for t in range(1,T+1):
    counter=0
    i=0
    print "Case #"+str(t)+":"
    while i<2**(N-2):
        #if i%10==0:
        #print "i:",i
        ok = True
        list=[]
        d={}
        v={}
        for base in range(2,11):
            a = getBaseVal(base,N,i)
            v[base]=a
            z=get_div(a)
            d[base]=z
            if (z<0):
                ok=False
                break
        if ok:
            print format(v[2],'b'),d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10]
        #print v
            counter=counter+1
        if (counter>=J):
            break
        i=i+1

