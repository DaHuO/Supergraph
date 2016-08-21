t=int(input())
ans=[]
for j in range(t):
	s=input()
	r=""+s[0]
	for i in s[1:]:
		if i>=r[0]:
			r=i+r
		else:
			r=r+i
	ans.append("Case #"+str(j+1)+": "+r)
for i in ans:
	print(i)

