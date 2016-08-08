from itertools import permutations
import sys

def solve(N,R,P,S):
    d = {
            "P": "PR",
            "R": "RS",
            "S": "PS"
    }
    for i in range(N-1):
        dn = dict()
        for v in d.itervalues():
            n = len(v)/2
            a = d[v[:n]]
            b = d[v[n:]]
            if a < b:
                dn[v] = a + b
            else:
                dn[v] = b + a
        d = dn

    for x in d.values():
        if x.count('P') == P and x.count('R') == R and x.count('S') == S:
            return x

    return "IMPOSSIBLE"

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        N,R,P,S = [int(x) for x in sys.stdin.readline()[:-1].split(" ")]
        res = solve(N,R,P,S)
        print "Case #%d: %s" % (i+1, res)

if __name__ == '__main__':
    main()
