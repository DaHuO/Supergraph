import sys

def next_number(num, N):
	s = format(num, 'b')
	if len(s) > (N - 2):
		return None
	prefix = "0" * (N - 2 - len(s))
	return "1" + prefix + s + "1"

def find_divisor(cand, n):
	cand = int(cand, n)

	p = 2
	while (p * p) <= cand:
		
		if cand % p == 0:
			return p
		p += 1	
	return None
	

_ = int(sys.stdin.readline())
N, J = [int(w) for w in sys.stdin.readline().split()]

num = 0
print "Case #1:"
while J > 0:
	cand = next_number(num, N)
	if cand is None:
		break
	ans = []

	for n in xrange(2, 11):
		divisor = find_divisor(cand, n)
		
		if divisor is None:
			break;
		ans.append(divisor)
	
	if len(ans) == 9:
		print cand, " ".join(map(str, ans))
		J -= 1
	
	num += 1