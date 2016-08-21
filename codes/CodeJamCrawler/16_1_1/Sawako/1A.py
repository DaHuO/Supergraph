for i in range(int(input())):
	s = list(input())
	l = s.pop(0)
	result = [l]
	while(len(s) > 0):
		c = s.pop(0)
		if c >= result[0]:
			result.insert(0, c)
		else:
			result.append(c)
	print("Case #{}: {}".format(i+1, ''.join(result)))