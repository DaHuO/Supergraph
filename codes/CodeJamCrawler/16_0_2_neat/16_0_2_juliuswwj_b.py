import sys

def sv(s, t):
    if s == '': 
        return 0
    if s[-1] == t:
        return sv(s[:-1], t)
    if t == '+':
        return sv(s[:-1], '-') + 1
    if t == '-':
        return sv(s[:-1], '+') + 1

for q in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    print "Case #%d: %d" % (q+1, sv(s, '+'))
