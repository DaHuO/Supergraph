m = 10**6 + 1

def solve(num):
	s = range(10)
	i = 1
	while s:
		num1 = num*i
		while num1:
			dig = num1%10
			if dig in s:
				s.remove(dig)
				if not s:
					return num*i
			num1 = num1/10

		i+=1
		num1 = num*i
	return num1
ans = ['INSOMNIA']
for i  in range(1,m):
	ans.append(solve(i))

t = int(raw_input())
for caseNr in xrange(1, t+1):
	n = int(raw_input())
	print("Case #%i: %s" % (caseNr, ans[n]))