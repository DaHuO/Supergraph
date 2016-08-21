def f(x,y,b):
    if y==1:
        return x
    return f(x,y-1,b)+(x-1)*b**(y-1)
t = int(raw_input())
for z in range(1, t+1):
    o = []
    [k,c,s]=map(int,raw_input().split())
    for i in range(1,k+1):
        o+=[f(i,c,k)]
    print "Case #{0}: {1}".format(str(z),' '.join(map(str,o)))
