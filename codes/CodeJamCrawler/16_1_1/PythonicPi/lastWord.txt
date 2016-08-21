L=map(str, raw_input().split())
for x in xrange(int(L[0])):
    res=''
    for y in L[x+1]:
        if res=='' or y>=res[0]:
            y+=res
            res=y
            
        else:
            res+=y
            
    print "Case #"+str(x+1)+": "+res      