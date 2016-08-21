import sys

lines = sys.stdin.readlines()
lines = map(str.strip, lines);

T = int(lines[0])

for i in xrange(1, T+1):
	K, C, S = map(int, lines[i].split())
	numbers = range(1, K**C + 1, K**(C-1))
	print "Case #" + str(i) + ": " + " ".join(map(str,numbers))