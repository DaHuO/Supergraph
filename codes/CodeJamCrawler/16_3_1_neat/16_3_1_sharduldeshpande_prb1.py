def maj(a):
	return sum(a)/2

def cnt(x,a):
	count = 0
	arr = []
	for i in xrange(len(a)):
		if(a[i]==x):
			count+=1
			arr.append(i)
	return arr




for _i in xrange(int(raw_input())):
	n = int(raw_input())
	a = map(int,raw_input().split())
	p = [0 for i in range(26)]
	ans = []
	for i in xrange(len(a)):
		p[i] = a[i]
	maxi = max(p)
	mcnt = cnt(maxi,p)
	s = ""
	while(sum(p)!=0):
		maxi = max(p)
		mcnt = cnt(maxi,p)		
		#print mcnt
		if(len(mcnt)==3):
			ans.append(p.index(maxi))
			s += chr(65+p.index(maxi))
			p[p.index(maxi)] -= 1
			s += " "
		elif(len(mcnt)==2):
			ans.append(mcnt[0])
			s += chr(65+p.index(maxi))

			p[mcnt[0]] -= 1
			ans.append(mcnt[1])
			s += chr(65+p.index(maxi))

			p[mcnt[1]] -= 1
			s += " "
		elif(len(mcnt)==1):
			ans.append(p.index(maxi))
			s += chr(65+p.index(maxi))
			p[p.index(maxi)] -= 1
			s += " "	
		else:
			ans.append(mcnt[0])
			s += chr(65+p.index(maxi))

			p[mcnt[0]] -= 1
			ans.append(mcnt[1])
			s += chr(65+p.index(maxi))

			p[mcnt[1]] -= 1
			s += " "
		#print p

	print "Case #"+str(_i+1)+": "+s










