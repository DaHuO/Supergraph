data=[]
with open('/Users/sb17/Downloads/D-small-attempt1.in') as f:
	for line in f:
		data.append([int(i) for i in line.split()])

f_t=open('/Users/sb17/Downloads/output_d.out','w')
t=data[0][0]
j=1
while(t>0):
	k,c,s=data[j]
	a=[]
	for i in xrange(1,k+1):
		a.append(i)
	f_t.write("Case #%d:"%j +" "+ ' '.join(str(num) for num in a))
	f_t.write('\n')
	j+=1
	t-=1
f_t.close()