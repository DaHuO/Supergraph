t = int(raw_input())  # read a line with a single integer
for x in xrange(1, t + 1):
    n=int(raw_input())
    d=[]
    nn=0
    ans=[]
    for i in xrange(2*n-1):
        d = d+[int(xx) for xx in raw_input().split(" ")]
    d.sort() 
    for ii in xrange(len(d)):
        nn=d.count(d[ii])
        if (nn%2 ==1):
            if not(d[ii] in ans):
                ans.append(d[ii])
#    ans.sort()
#    print ans
    print "Case #{}:".format(x),
    for jj in xrange(len(ans)):
        print ans[jj],
    print

