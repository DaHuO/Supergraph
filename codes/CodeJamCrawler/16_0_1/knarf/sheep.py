import sys
from time import sleep

def add_to_seen(seen, s):
	newly_seen = 0
	for d in s:
		if not d in seen:
			seen[d] = True
			newly_seen+=1
	return newly_seen,seen

def count_sheep(n):
	if n==0:
		return "INSOMNIA"
	digits_seen = {}
	left_to_see = 10
	curr = n
	while left_to_see > 0:
		newly_seen, digits_seen = add_to_seen(digits_seen, str(curr))
		left_to_see -= newly_seen
		curr+=n
	return curr-n

t = int(sys.stdin.readline())
i = 1
for l in sys.stdin:
	n = int(l.strip())
	print "Case #{0}: {1}".format(i,count_sheep(n))
	i+=1
