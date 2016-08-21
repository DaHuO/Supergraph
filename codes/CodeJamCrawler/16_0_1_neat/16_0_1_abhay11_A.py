numRuns=int(input())
for i in range(numRuns):
	k=int(input())
	if k==0:
		print("Case #"+str(i+1)+": INSOMNIA")
		continue
	digits=[False]*10
	seen=0
	for j in range(1,10000000):
		a=j*k
		while a>0:
			if not(digits[a%10]):
				digits[a%10]=True
				seen+=1
			a//=10
		if seen==10:
			print("Case #"+str(i+1)+": "+str(j*k))
			break
	if seen<10:
		print("Case #"+str(i+1)+": INSOMNIA")