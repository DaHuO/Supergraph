import sys

def solve(n):
    num = n
    digits = set()
    while len(digits) != 10:
        for i in str(num):
            if i not in digits:
                digits.add(i)
        num += n
    return num - n;

for cases in xrange(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if (n == 0):
        print "Case #%d: INSOMNIA"%(cases+1)
    else:
        print "Case #%d: %d"%(cases+1,solve(n))
    
    
