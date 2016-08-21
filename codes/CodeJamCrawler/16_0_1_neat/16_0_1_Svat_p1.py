import sys

def solve(s):
	init = int(s)
	if init == 0:
		return "INSOMNIA"
	digitsseen = set([c for c in s])
	x = init
	while True:
		if len(digitsseen) == 10:
			break
		x = x + init
		s = str(x)
		digitsseen = digitsseen | set([c for c in s])
	return str(x)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    N = int(f.readline().strip())
    for i in xrange(N):
        x = solve(f.readline().strip())
        print("Case #%d: %s" % (i+1, x))