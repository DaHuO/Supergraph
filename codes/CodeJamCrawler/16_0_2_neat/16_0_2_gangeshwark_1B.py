def count(str):
	cnt=0
	str=list(str)
	n=len(str)
	i=1
	j=0
	while(True):
		if str[0]=='+':
			i=1
			for x in xrange(1,n):
				if str[x]=='+':
					i+=1
				else:
					break
			if i!=n:
				cnt+=1
				for x in xrange(i):
					str[x]='-'
			else:
				return cnt

		elif str[0]=='-':
			i=1
			for x in xrange(1,n):
				if str[x]=='-':
					i+=1
				else:
					break
			cnt+=1
			for x in xrange(i):
				str[x]='+'


if __name__ == '__main__':
	n=int(raw_input())
	for i in xrange(n):
		print "Case #%d: "%(i+1) + str(count(raw_input()))