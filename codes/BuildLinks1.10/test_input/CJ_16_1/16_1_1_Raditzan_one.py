import sys

def solve(n):
    l = ""
    for i in n:
        if len(l)==0:
            l=i
        else:
            if i>=l[0]:
                l = i+l
            else:
                l=l+i

    return l

n = int(raw_input())

for i in xrange(1,n+1):
    string = raw_input()
    output = solve(string)

    print "Case #%d: %s" % (i,output)