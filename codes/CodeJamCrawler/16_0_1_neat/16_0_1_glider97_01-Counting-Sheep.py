import sys

def lastMul(n):
	n = int(n)
	if not n:
		return n
	else:
		nums = []
		t = n
		while True:
			for i in str(t):
				if i not in nums:
					nums.append(i)
			if all([True if i in nums else False for i in '1234567890']):
				return t
			t += n

infile = sys.argv[1]
with open(infile) as f:
	t = int(f.readline())
	for x in xrange(t):
		res = lastMul(f.readline())
		res = str(res) if res else "INSOMNIA"
		with open(infile[:-2] + 'out', 'a') as g:
			g.write("Case #" + str(x + 1) + ': ' + res + '\n')
