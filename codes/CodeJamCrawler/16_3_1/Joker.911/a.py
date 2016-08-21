from string import ascii_uppercase
from collections import OrderedDict
od = OrderedDict((ch, idx) for ch, idx in enumerate(ascii_uppercase, 1))

def maxi(a,n):
	idx=list()
	
	ma=max(a)

	for k in range(len(a)):
		if len(idx)==2:
			return idx
		if ma == 1 and len(idx)==1 and n>2:
			return idx
		if a[k]>=ma:
			idx.append(k)
	return idx

with open('A-test.in','r') as f:
	t=int(f.readline())
	for i in range(1,t+1):
		n=int(f.readline())
		st=f.readline().split()
		nu=list()
		for j in range(n):
			nu.append(int(st[j]))
		su=sum(nu)

		
		print("Case #"+str(i)+": ",end=" ")
		
		while su>0:
			m=list()
			m=maxi(nu,n)
			
			for jk in range(len(m)):
				print(od[m[jk]+1],end="")
				nu[m[jk]]-=1
				if nu[m[jk]]==0:
					n-=1
			print(" ",end="")

			su=sum(nu)
		print("")





