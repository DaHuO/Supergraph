def solve(arr, n):
	d = {}
	ans = ''
	if n!= 2:
		for i,j in enumerate(arr):
			d[chr(i+65)] = j 
		while sum(d.values()) >2 :
			el = max(d, key = d.get)
			d[el] -= 1
			ans += el + " "
		tmp = []
		for k, v in d.iteritems():
			if v==1:
				tmp.append(k)
		ans+= "".join(tmp)
	else:
		s = sum(arr)
		ans = 'AB '*(s/2)
	return ans
t = int(raw_input())
for caseNr in xrange(1, t+1):
	n = int(raw_input())
	arr = map(int, raw_input().split())

	print("Case #%i: %s" % (caseNr, solve(arr, n)))







