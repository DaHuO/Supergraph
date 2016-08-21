def fun(n,i,s):
    st=set(map(int,str(n*i)))
    for j in st:
        if j in s:
            s.remove(j)
    if len(s)==0:
        return True
    else:
        return False
tc=int(raw_input())
for case in range(1,tc+1):
    n=int(raw_input())
    s=[i for i in range(10)]
    i=1
    if n==0:
        print "Case #"+str(case)+": "+"INSOMNIA"
    else:
        while True:
            f=fun(n,i,s)
            if f:
                break
            else:
                i=i+1
        print "Case #"+str(case)+": "+str(n*i)
        
