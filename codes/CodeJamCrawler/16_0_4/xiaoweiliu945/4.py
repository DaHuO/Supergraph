t = int(raw_input())

for i in xrange(t):
	k, c, s = [int(x) for x in raw_input().split(' ')]
	res_list = ''
	for j in range(s):
		res_list += str(j+1) + ' '
	res_list.strip()
	print 'Case #%d: %s'%((i+1), res_list)
