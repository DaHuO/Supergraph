N = int(input())

for i in range(N) :
	s=input()
	k=0
	t=s[0]
	for c in s:
		if ((c=="+") and (t=="-")) or ((c=="-") and (t=="+")):
			k=k+1
		t=c
	if c=="-":
		k=k+1
	print('Case #'+str(i+1)+': '+str(k))


