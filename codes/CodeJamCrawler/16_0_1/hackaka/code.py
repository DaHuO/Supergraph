a = input();
b = []
for i in range(a):
	b.append(input())


def geta(n):
	seen = []
	k = 0
	l = 1
	while(1):
		q = n*l
		qq = list(str(q))
		for h in qq:
			seen.append(h)
		seen = sorted(set(seen))
		cop = ['0','1','2','3','4','5','6','7','8','9']
		if seen==cop:
			return q
			break						
		l=l+1
		if l>=100000:
			return "INSOMNIA"
			break	


kk = 1
for j in b:
	print("Case #"+str(kk)+": "+str(geta(j)))
	kk = kk+1