def solve(num):
	if num == 0:
		return 'INSOMNIA'
	d = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	i = 1
	while d:
		mynum = num * i
		tmp = mynum
		while tmp > 0:
			l = tmp % 10
			if l in d:
				d.remove(l)
			tmp /= 10
		i += 1
	return str(mynum)

caseNum = int(raw_input())
for i in range(caseNum):
	print 'Case #%d: %s' % (i+1, solve(int(raw_input())))