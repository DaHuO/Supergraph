def go():
    f=open('A-large.in')
    c=int(f.readline())
    for case in range(1,c+1):        
        print 'Case #%d:'%case,
        print solve(f.readline())
    f.close()

    

def solve(s):
    n=int(s)
    n1=n
    m=2
    l=[0]*10
    while m<10000 and (not all(l)):
        ns=str(n1)
        for x in range(10):
            if str(x) in ns:
                l[x]+=1
        if all(l):
            return n1
        n1=n*m
        m+=1
    return 'INSOMNIA'

    
        
