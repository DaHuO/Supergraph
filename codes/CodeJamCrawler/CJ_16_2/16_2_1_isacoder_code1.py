
from collections  import defaultdict

def subtract(d, charlist, times):
	
	for c in charlist:
		d[c] -= times	
	return d


def calc(s):
	d = defaultdict(int)
	hist = d
	for c in s:
		d[c] += 1

	result = ([0]*hist['Z'])
	d = subtract(d,'ZERO', hist['Z'])
	result += ([6]*hist['X'])
	d = subtract(d,'SIX', hist['X'])
	result += ([8]*hist['G'])
	d = subtract(d,'EIGHT', hist['G'])
	result += ([2]*hist['W'])
	d = subtract(d,'TWO', hist['W'])
	result += ([4]*hist['U'])
	d = subtract(d,'FOUR', hist['U'])
	result += ([7]*hist['S'])
	d = subtract(d,'SEVEN', hist['S'])
	result += ([3]*hist['R'])
	d = subtract(d,'THREE', hist['R'])
	result += ([1]*hist['O'])
	d = subtract(d,'ONE', hist['O'])
	result += ([9]*(hist['N']/2))
	d = subtract(d,'NINE', hist['N']/2)
	result += ([5]*hist['V'])
	d = subtract(d,'FIVE', hist['V'])
	return ''.join(map(str,sorted(result)))

t = int(raw_input())  
for i in xrange(1,t+1):
  s = raw_input()
  print "Case #{}: {}".format(i, calc(s))
  