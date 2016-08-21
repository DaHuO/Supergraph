
import sys
data = map(int,sys.stdin.readlines())
n = data[0]
data = data[1:]
def add_digits(x,d):
    while x > 0:
        d.add(x%10)
        x = x /10

for (i,x) in enumerate(data):
    sseen = set()
    digits = set()
    p = x
    while( p not in sseen and len(digits) != 10):
        sseen.add(p)
        add_digits(p,digits)
        p += x
    if p in sseen and len(digits) != 10:
        print "Case #{0}: INSOMNIA".format(i+1)
    else:
        print "Case #{0}: {1}".format(i+1,p-x)
