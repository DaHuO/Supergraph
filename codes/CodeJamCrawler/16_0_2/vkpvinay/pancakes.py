# your code goes here
for i in range(1,int(input())+1):
	s=input()
	t=c=s[0]
	count=0
	for e in s:
		if c!=e:
			count+=1
			c=e
	if (count%2==0 and t=='-') or (count%2!=0 and t=='+'):
		count+=1
	print('Case #{:d}: {:d}'.format(i,count))