t = int(raw_input())
cnt = 0
while cnt<t:
	cnt+=1
	k,c,s = [int (i) for i in raw_input().split()]
	print 'Case #%d:'%cnt,
	for i in range(1,k+1):
		print i,
	print