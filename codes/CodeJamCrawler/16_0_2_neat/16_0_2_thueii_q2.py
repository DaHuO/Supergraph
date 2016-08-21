import sys

def g(s):
    while len(s) > 0 and s[-1] == '+':
        s = s[:-1]
    sign_change = 0
    last_sign = '+'
    for i in range(0, len(s)):
        if s[-(i+1)] != last_sign:
            sign_change += 1
        last_sign = s[-(i+1)]
    return sign_change

l = sys.stdin.readline()
m = int(l.strip())

for i in range(0, m):
    l = sys.stdin.readline()
    s = l.strip()
    print("Case #%d: %d" % (i + 1, g(s)))

