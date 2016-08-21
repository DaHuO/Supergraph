import sys

vals = sys.stdin.read().split('\n')[:-1]
num_vals = vals[0]
vals = vals[1:]

badstring = "INSOMNIA"

def sheep(n):
	if n == 0:
		return badstring
	i = 1
	curval = n*i
	digits = set()
	while True:
		digits.update(str(curval))
		if len(digits)==10:
			return curval
		i += 1
		curval = n*i
		
vals = map(int, vals)
results = map(sheep, vals)

for i in xrange(len(results)):
	print "Case #"+str(i+1)+": "+str(results[i])
