f=open("A-large.in",'r')
m=int(f.readline())
for vv in range(m):
    b=f.readline()
    
#OZONETOWER
    a=list(b)
    y=""
    while('Z' in a):
        for i in "ZERO":
            p=a.index(i)
            del(a[p])
        y=y+"0"
    
    while('W' in a):
        for i in "TWO":
            p=a.index(i)
            del(a[p])
        y=y+"2"
    while(('U' in a)):
        for i in "FOUR":
            p=a.index(i)
            del(a[p])
        y=y+"4"
    while('X' in a):
        for i in "SIX":
            p=a.index(i)
            del(a[p])
        y=y+"6"
    while('G' in a):
        for i in "EIGHT":
            p=a.index(i)
            del(a[p])
        y=y+"8"
    while(('H' in a)):
        for i in "THREE":
            p=a.index(i)
            del(a[p])
        y=y+"3"
    while(('S' in a)):
        for i in "SEVEN":
            p=a.index(i)
            del(a[p])
        y=y+"7"

    while(('V' in a)):
        for i in "FIVE":
            p=a.index(i)
            del(a[p])
        y=y+"5"
    while(('O' in a)):
        for i in "ONE":
            p=a.index(i)
            del(a[p])
        y=y+"1"
    while(('I' in a)):
        for i in "NINE":
            p=a.index(i)
            del(a[p])
        y=y+"9"
        
    u=list(y)
    u.sort();
    c=''.join(u)
    print "Case #"+str(vv+1)+": "+str(c)
