import sys

def update(x, seen):
	y = x
	while (y > 0):
		seen[y%10] = True
		y /= 10

lines = sys.stdin.readlines()

lines = map(str.strip, lines);

T = int(lines[0])

for i in xrange(1, T+1):
	n = int(lines[i])
	seen = [False] * 10
	tmp = n

	if n == 0:
		print "Case #" + str(i) + ": INSOMNIA"
		continue

	ans = 0
	while not all(seen):
		ans += 1
		update(tmp, seen)
		tmp += n

	print "Case #" + str(i) + ": " + str(ans * n)
