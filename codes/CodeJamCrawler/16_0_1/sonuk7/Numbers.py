t=int(input())
for _t in range(t):
    a=int(input())
    #a=_t
    if a==0:
        print "Case #"+str(_t+1)+": "+'INSOMNIA'
        continue
    else:
        s=set()
        v=a
        while len(s)!=10:
            a1=str(a)
            for i in list(a1):
                s.add(i)
            a+=v
            #print a,s
        print "Case #"+str(_t+1)+": "+str(a-v)
