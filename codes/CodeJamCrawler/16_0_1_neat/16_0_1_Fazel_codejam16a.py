#T = int(raw_input())
from io import open
f = open("A-large.in")
T = int(f.readline())
def digitz(n):
    digits = set()
    while(n > 0):
        digits.add(n%10)
        n /= 10
    #print digits
    return digits
nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
def solve(t):
    seen = set()
    n = 1
    while seen != nums :
        seen |= digitz(t*n)
        #print seen
        n += 1
    return t*(n-1)
g  = open("aaa2.txt", "w")
for i in xrange(T):
    inp = int(f.readline())
    if inp == 0 :
        g.write(u"Case #{0}: INSOMNIA\n".format(i+1))
    else:
        g.write( u"Case #{0}: {1}\n".format(str(i+1), str(solve(inp))))

# for i in range(1, 1000000):
#     print solve(i)
f.close()
g.close()