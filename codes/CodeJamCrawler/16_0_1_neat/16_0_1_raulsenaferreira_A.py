import sys

N=1000000
T = int(input())

for i in range(0,T):
	x=int(input())
	arr=[]
	res = [0,0,0,0,0,0,0,0,0,0]
	cont=0
	
	for j in range(1,N+1):
		a = x*j
		arr = [int(y) for y in str(a)]

		for k in arr:
			res[k]=1
		soma = sum(res)
		if soma==10:
			print("Case #{}: {}".format(i+1, a))
			break
		elif j==N and soma!=10:
			print("Case #{}: INSOMNIA".format(i+1))
