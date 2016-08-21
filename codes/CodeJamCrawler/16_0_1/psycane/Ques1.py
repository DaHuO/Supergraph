from sys import stdin as ip
f=open('op.txt',"w")
for _ in xrange(int(ip.readline())):
    n=int(ip.readline())
    if n==0:
        f.write("Case #%d: INSOMNIA\n"%(_+1))
        continue
    s=set(['1','2','3','4','5','6','7','8','9','0'])
    s1=set(list(str(n)))
    i=1
    while s1!=s:
        i+=1
        k=i*n
        s1=s1.union(set(list(str(k))))
    f.write("Case #%d: %d\n"%(_+1,n*i))
f.close()
