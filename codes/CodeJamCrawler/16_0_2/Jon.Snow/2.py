def findright(s):
	i=len(s)-1
	while(i>=0 ):
		if s[i]=='-':
			return i
		i-=1
	return i	

def find_changes(s):
	s=list(s)
	count=0
	j=findright(s)
	while(j>=0):
		if s[0]=='+':
			i=0
			count+=1
			while(s[i]=='+'):
				s[i]='-'
				i+=1
		temp=list()
		count+=1
		for m in xrange(j):
			var=s[j-m]
			if var=='+':temp.append('-')
			else:temp.append('+')
		s=temp
		j=findright(s)
	return count


t,case=input(),1
while(t>0):
	s1=raw_input()
	print 'Case #'+str(case)+':',find_changes(s1)
	case+=1
	t-=1
