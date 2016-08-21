def div(x):
	y=2
	while y*y<=x:
		if x%y==0:
			return y
		y+=1
	return 1

def con(x,y):
	z=0
	yy=1
	while x:
		z+=(x%2)*yy
		yy*=y
		x/=2
	return z


ans = []

for x in xrange(2**15+1,2**16,2):
	k=1
	for y in xrange(2,11):
		if k==1:
			if div(con(x,y))==1:
				k=0
	if k==1:
		ans.append(x)
	print x,len(ans)
	if len(ans)==50:
		break

def bins(x):
	if x>0:
		return bins(x/2)+str(x%2)
	return ""

for x in ans:
	print bins(x),
	for y in xrange(2,10):
		print div(con(x,y)),
	print div(con(x,10))


