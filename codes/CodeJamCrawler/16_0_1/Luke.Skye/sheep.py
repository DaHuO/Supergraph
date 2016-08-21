c=[0]*10;

def scount(n):
    x=str(n)
    for a in x:
        c[int(a)-1]+=1
    
j=1
fr=open("output.txt","w")
fo=open("A-large.in","r")
t=int(fo.readline())
while j<=t:
    i=1
    a=int(fo.readline())
    while True:
        if a==0:
            break
        scount(i*a)
        if 0 not in c:
            break
        i+=1
    if 0 in c:
        fr.write("Case #%d: INSOMNIA\n" %j)
    else:
        fr.write("Case #%d: %d\n" %(j,i*a))
    c=[0]*10;
    j+=1

