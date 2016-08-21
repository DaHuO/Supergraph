import sys

stream = sys.stdin

t = int(stream.readline().strip())

def count(s):
    n = len(s)
    if n==1:
        return 0 if s[0]=='+' else 1
    count = 0 if s[-1]=='+' else 1
    pos = -2
    while -n<=pos:
        if s[pos]!=s[pos+1]:
            count += 1
        pos -= 1
    return count

for i in range(t):
    s = stream.readline().strip()
    print 'Case #' + str(i+1) + ':', count(s)
