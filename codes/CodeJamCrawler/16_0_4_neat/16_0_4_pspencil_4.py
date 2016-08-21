t = int(raw_input())
for i in range(1,t+1):
    print "Case #"+str(i)+":",
    k = int(raw_input().split(' ')[0])
    print ' '.join([str(x) for x in range(1,k+1)])
