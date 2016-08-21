def solve(a):
	ans = 1 if a[0]=="-" else 0
	for i in xrange(1,len(a)):
		if a[i] == "-" and a[i-1] == "+":
			ans += 2
	return ans
	
inputs = []
for _ in xrange(input()):
	inputs.append(raw_input())

for i, s in enumerate(inputs):
	print "Case #%d:"%(i+1),solve(s)