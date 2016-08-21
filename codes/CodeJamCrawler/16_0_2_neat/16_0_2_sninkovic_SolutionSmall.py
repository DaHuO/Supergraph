
def solve2(s):
    prviplus=True
    last='+'
    rv=0
    if s[-1]=='-':
        prviplus=False
        last = '-'
        rv=1
    
    for i in range(len(s)-1, -1,-1):
        if s[i]!=last:
            rv=rv+1
            last=s[i];
    return rv

T = int(raw_input())
for t in range(0,T):
    s = raw_input()
    #print "ucitan ",s
    rv=solve2(s)
    print "Case #"+str(t+1)+": "+str(rv)
    

