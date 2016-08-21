f=open('/Users/sb17/Downloads/B-large.in')
data=f.read().splitlines()
f_t=open('/Users/sb17/Downloads/output_b.out','w')
t=int(data[0])
k=1
while(t>0):
	a=data[k]
	flips=0
	if(a[0]=='+'):
		previous='+'
	else:
		previous='-'
	for i in range(1,len(a)):

		if a[i]!=previous:
			flips+=1
			if(previous=='+'):
				previous='-'
			else:
				previous='+'
	if previous=='-':
		flips+=1
	f_t.write("Case #%d: %d" %(k,flips))
	f_t.write('\n')
	k=k+1
	t=t-1
f_t.close()
