t=int(input())
x=1
for _ in range(t):
	l1=list(); l2=list()
	l=list()
	s=input()
	for _ in range(len(s)):
		if _==0:
			l1.append(s[_]); l2.append(s[_])
		else:
			for a in range(len(l1)):
				l1[a]=s[_]+l1[a]
			for b in range(len(l2)):
				l2[b]=l2[b]+s[_]
			temp=list()
			temp.extend(l1); l1.extend(l2); l2.extend(temp)
	l.extend(l1); l.extend(l2)
	l.sort()
	print("Case #{}: {}".format(x,l.pop()))
	x=x+1;