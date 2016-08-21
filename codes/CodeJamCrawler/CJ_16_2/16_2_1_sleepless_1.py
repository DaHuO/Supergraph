def q(a):
	return ord(a)-ord('A')
digits=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
for t in range(int(input())):
	a=list(input())
	b=[0]*26
	for i in a:
		b[q(i)]+=1
	c=[0]*10
	while(b[25]>0):
		c[0]+=1
		for j in digits[0]:
			b[q(j)]-=1
	while(b[q('W')]>0):
		c[2]+=1
		for j in digits[2]:
			b[q(j)]-=1
	while(b[q('X')]>0):
		c[6]+=1
		for j in digits[6]:
			b[q(j)]-=1
	while(b[q('S')]>0):
		c[7]+=1
		for j in digits[7]:
			b[q(j)]-=1
	while(b[q('V')]>0):
		c[5]+=1
		for j in digits[5]:
			b[q(j)]-=1
	while(b[q('F')]>0):
		c[4]+=1
		for j in digits[4]:
			b[q(j)]-=1
	while(b[q('R')]>0):
		c[3]+=1
		for j in digits[3]:
			b[q(j)]-=1
	while(b[q('H')]>0):
		c[8]+=1
		for j in digits[8]:
			b[q(j)]-=1
	while(b[q('I')]>0):
		c[9]+=1
		for j in digits[9]:
			b[q(j)]-=1
	while(b[q('N')]>0):
		c[1]+=1
		for j in digits[1]:
			b[q(j)]-=1
	#print(c,b
	print("Case #"+str(t+1)+": ",end='')
	for i in range(10):
		for j in range(c[i]):
			print(i,end='')
	print()
	