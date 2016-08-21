def doIt(n) :
	if n == 0 :
		return "INSOMNIA"
	numbers = [0,1,2,3,4,5,6,7,8,9]
	i = 1
	while len(numbers) > 0 :
		x = i * n
		remv = list(str(x))
		for r in remv :
			r = int(r)
			if r in numbers :
				numbers.remove(r)
		i+=1
	i-=1
	return str(n*i)
numOfCases = int(input())
cases = []
for i in range(numOfCases) :
	cases.append(int(input()))

for i,case in enumerate(cases) :
	print "Case #%d: %s" % (i+1, doIt(case))