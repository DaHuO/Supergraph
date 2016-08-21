from collections import Counter
for _ in range(int(input())):
	n=int(input())
	ls=list()
	for __ in range(2*n-1):
		ls.extend(input().split())
	c=Counter(ls)
	ans=list()
	for k,v in c.items():
		if int(v)%2!=0:
			ans.append(int(k))
	print ("Case #{}: ".format(_+1),end="")
	print (*sorted(ans))
			
