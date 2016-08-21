def sheep_count(n):
	ocurred=set()
	for i in range(200):
		num=(i+1)*n
		ocurred.update(set(str(num)))
		if(len(ocurred))==10:
			return num
	return -1

n_testcase=int(raw_input())
for i in range(n_testcase):
	n=int(raw_input())
	ans=sheep_count(n)
	print 'Case #%d:' %(i+1),
	if ans>=0:
		print ans
	else:
		print 'INSOMNIA'
	