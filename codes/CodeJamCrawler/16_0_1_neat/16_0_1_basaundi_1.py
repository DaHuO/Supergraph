import sys

def case(N):
    if N == 0:
        return "INSOMNIA"
    seen = set()
    i = 1
    while i < 10000:
        counted = N*i
        digits = set("%d"%(counted))
        seen |= digits
        if len(seen) == 10:
            return counted
        i += 1
    return "INSOMNIA"

def main(inps=None):
    if not inps:
        inps = sys.stdin
        
    lines = iter(inps)
    T = int(next(lines))
    for i in range(T):
        N = int(next(lines))
        print "Case #%d: %s"%(i + 1, str(case(N)))
        


if __name__ == "__main__":
    main(sys.stdin)
