t = int(raw_input())

for i in range(t):
	n = int(raw_input())
	odd = []
	for j in range(2*n-1):
		lst = map(int, raw_input().split())
		for x in lst:
			if x not in odd:
				odd.append(x)
			else:
				odd.remove(x)
	odd = sorted(odd)
	result = str(odd[0])
	for x in odd[1:]:
		result += ' '+str(x)
	print "Case #{}: {}".format(i+1, result)
