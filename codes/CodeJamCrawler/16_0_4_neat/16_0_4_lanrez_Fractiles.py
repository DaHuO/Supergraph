def gold(k,c):
    if (c == 1):
        a = ' '.join([str(x+1) for x in range(0,k)])
        return a
    elif(k==1):
        return '1'
    else:
        a = ' '.join([str(x+1) for x in range(1,k)])
        return a

        
def fractiles(file):
    f=open(file)
    g=open('output.ou',mode='w')
    b=int(f.readline()[:-1])
    for x in range(b):
        (m,a,c)=f.readline()[:-1].split(' ')
        m=int(m)
        a=int(a)
        c=int(c)
        v = gold(m,a)
        g.write("Case #"+str(x+1)+": "+ v +"\n")
    f.close()
    g.close()
