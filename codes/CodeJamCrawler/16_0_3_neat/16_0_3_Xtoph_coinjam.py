n = 32
j = 500
maxlen = (n - 4)/2

a = 11

def fill(length):
	if length == 1:
		return [0, 10]
	return fill(length - 1) + [10**(2*length - 1) + x for x in fill(length - 1)]

b = fill(maxlen)[:j]
c = [10**(n-2) + 1 + 10 * x for x in b]

res = [a*x for x in c]
print "Case #1:"
for r in res:
	print str(r) + " 3 4 5 6 7 8 9 10 11"