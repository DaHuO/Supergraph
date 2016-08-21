import sys

def solve(K,C,S):
	return ' '.join(map(str, range(1,S+1)))

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline().strip())
    for i in xrange(T):
    	[K,C,S] = map(int, f.readline().strip().split(' '))
        x = solve(K,C,S)
        print("Case #%d: %s" % (i+1, x))