import sys

def solve(x):
    if x == 0:
        return "INSOMNIA"
    else:
        s = set([])
        r = x
        i = 1
        while True:
            r = i*x
            s|=set(str(r))
            if len(s)==10:
                return r
            i += 1

with open(sys.argv[1]) as fh:
    N = int(fh.readline().rstrip())
    for i in range(N):
        x = int(fh.readline().rstrip())
        print("Case #{0}: {1}".format(i+1, solve(x)))
