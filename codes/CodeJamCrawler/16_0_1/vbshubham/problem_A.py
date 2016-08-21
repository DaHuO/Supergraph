t = int(raw_input())
cnt=0
while cnt<t:
	cnt+=1
	n = int(raw_input())
	if n == 0:
		print 'Case #%d: INSOMNIA'%cnt
		continue
	digits = set([])
	cur = 0
	while len(digits)<10:
		cur +=n
		digits |= set(list(str(cur)))
		# print '\t',cur,digits
	print 'Case #%d:'%cnt,cur