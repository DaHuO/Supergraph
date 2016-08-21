
n = raw_input()

for i in range(0, int(n)):
    a = raw_input().split()
    k = int(a[0])
    c = int(a[1])
    s = int(a[2])
    o = ''
    for j in range(0, k):
        o += ' ' + str(j+1)
    print "Case #%d:%s" %(i+1, o)
    
