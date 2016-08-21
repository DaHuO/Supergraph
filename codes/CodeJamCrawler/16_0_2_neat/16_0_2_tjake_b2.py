n = input()
for t in xrange(n):
    print "Case #%d:"%(t+1),

    s = raw_input()
    count = 0
    for i in xrange(len(s)-1):
        if s[i]!=s[i+1]:
            count += 1
    print count if s[-1]=="+" else count+1
