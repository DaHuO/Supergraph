import sys
import itertools

def ans(n):
	if not n:
		return "INSOMNIA"

	x = n
	seen = [0 for i in xrange(0,10)]
	while True:
		xx = x
		while xx:
			seen[xx%10] = 1
			xx = xx/10
		if sum(seen) == 10:
			return x
		x = x + n
	return -1

def main():
	s = sys.stdin.readline()
	T = int(s)
	for i in xrange(0,T):
		s = sys.stdin.readline()
		n = int(s)

		print "Case #{0}: {1}".format(i+1, ans(n))

if __name__ == "__main__":
	main()
