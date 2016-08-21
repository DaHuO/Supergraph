def oord(s): return ord(s)-ord("A")
def solve(n,s):
	R=[]
	while sum(s)>0:
		r=""
		x=max(s)
		if s.count(x)>1:
			if x==1 and s.count(x)==3:
				r+=chr(s.index(x)+ord("A"))
				s[s.index(x)]-=1
			else:
				c=0
				for i in range(n):
					if s[i]==x:
						s[i]-=1
						r+=chr(i+ord("A"))
						c+=1
						if c==2: break
		else:
			r+=chr(s.index(x)+ord("A"))
			s[s.index(x)]-=1
		R.append(r)
	return R

testcase = input()
for i in range(testcase):
    print "Case #"+str(i+1)+":",
    N=input()
    S=map(int,raw_input().split())
    print " ".join(solve(N,S))
