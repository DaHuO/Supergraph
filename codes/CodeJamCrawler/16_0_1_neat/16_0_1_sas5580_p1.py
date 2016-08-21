import sys
sys.stdin = open("A-large.in","r")
sys.stdout = open("OP.txt","w")

for asd in xrange(int(raw_input().strip())):
    y = int(raw_input().strip())
    ans = [False for i in xrange(10)]

    x = 0
    for i in xrange(100):
        x+=y
        for d in str(x):
            ans[int(d)] = True

        if (not (False in ans)): break       
        
        

    if (not (False in ans)): print "Case #%d: %d"%(asd+1,x)
    else: print "Case #%d: INSOMNIA" %(asd+1)
    

