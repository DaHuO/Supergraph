import sys

T = int(sys.stdin.readline())
for i in range(0,T):
    w = int(sys.stdin.readline())

    # double check
    if w == 0:
        print("Case #%d: INSOMNIA" % (i+1))
    else:
        digits = set()
        k = 0
        while len(digits) != 10:
            k += 1
            digits = digits | set(str(k*w))
        print("Case #%d: %d" % (i+1, w*k))
