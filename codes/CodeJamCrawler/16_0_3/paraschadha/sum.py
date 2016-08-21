import math
def factor(n):
	rt = math.sqrt(n)
	i = 2
	while i<=min(rt, 1000000):
		if n%i==0:
			return i
		i+=1
	return 1;

def convert(s,b):
	ans=0
	t=1
	i = len(s)-1
	while i>=0:
		if s[i]=='1':
			ans += t
		t *= b
		i-=1
	return ans

T = long(raw_input())
cas = 1
while cas<=T:
	arr = map(long, raw_input().split(" "))
	N = arr[0]
	J = arr[1]
	
	init = ["1"]
	for i in range(N-2):
		init.append("0")
	init.append("1")
	
	print "Case #"+str(cas)+":"
	total=0
	
	i=0
	while i<2**N-2 and total<J:
		s = []
		
		for j in range(len(init)):
			s.append(init[j])
		
		t = i
		
		j=N-2
		while j>0:
			if t%2==1:
				s[j] = '1'
			t /= 2
			j -= 1
		f=1
		arr=[]
		
		j=2
		while j<11:
			t = convert(s, j)
			x = factor(t)
			if x==1:
				f=0
				break
			else:
				arr.append(x)
			j += 1
		
		if f==1:
			print "".join(s),
			j=0
			while j<len(arr):
				print str(arr[j]),
				j+=1
			print ""
			total += 1
		i += 1
	cas += 1
