def gen(n,b):
    v = bin(n)[2:]
    l = ((b/2)-1)-len(v)
    v = '1' + ('0'*int(l)) + v
    mv = v + v[::-1]
    dv = '3 4 5 6 7 8 9 10 11'
    return mv + " " + dv

def jam(file):
    f=open(file)
    g=open('output.ou',mode='w')
    b=int(f.readline()[:-1])
    for x in range(b):
        (m,a)=f.readline()[:-1].split(' ')
        m = int(m)
        a = int(a)
        g.write("Case #"+str(x+1)+":\n")
        for i in range (a):
            g.write(gen(i,m)+"\n")
    f.close()
    g.close()
