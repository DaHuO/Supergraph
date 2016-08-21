import sys
sys.stdin = open("D-small-attempt0.in", "r")
sys.stdout = open("d-out.txt", "w")
t=input()
for case in xrange(1, t+1):
    k,c,s = map(int, raw_input().split())
    print "Case #%d:" %case,
    i = 1
    while i < k**c + 1:
    #for i in xrange(1, k**c+1, k**(c-1)):
        print i,
        i += k**(c-1)
    print ''
