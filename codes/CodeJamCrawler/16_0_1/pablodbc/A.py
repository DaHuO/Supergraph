def f(N):
	k = int(N)
	while k > 0:
		h[k%10] = True
		k//=10
t = int(input())
for i in range(t):
	N = int(input())
	if N == 0 : print("Case #"+str(i+1)+": INSOMNIA")
	else:
		h = 10*[False]
		j = 1
		res = 1
		while True:
			f(N*j)
			if any(h[i] == False for i in range(10)) : res+=1
			else : break
			j+=1
		print("Case #"+str(i+1)+":",N*res)