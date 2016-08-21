import sys

T = int(sys.stdin.readline())
for i in range(T):
    s = list(sys.stdin.readline().strip())
    now = s[0]
    flips = 0
    for c in s:
        if c != now:
            flips += 1
            now = c
    if now != "+":
        flips += 1
    print "Case #%d: %d" % (i+1, flips)
