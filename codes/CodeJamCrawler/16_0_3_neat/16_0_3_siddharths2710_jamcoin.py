import itertools
def prime(n):
	j = 2
	while j*j <= n:
		if n % j == 0 :
			return False
		j = j + 1
	return True

def fn(x):
	for i in range(2,11):
		if prime(int(x,i)):
			return False
	return True
def div(x):
	res=[]
	for i in range(2,11):
		temp = int(x,i)
		j=2
		while j*j<=temp:
			if temp % j == 0:
				res.append(j)
				break
			j = j + 1
	return res
		
t = int(input())
for x in range(t):
	(n,j) = input().split()
	n = int(n)
	j = int(j)
	print("Case #",x+1,":",sep='')
	l = list(filter(lambda x: x[0] == '1' and x[-1] == '1' and fn(x),["".join(list(i)) for i in itertools.product(['0', '1'], repeat=n)]))
	print(l)
"""
	for i in range(j):
		print(l[i],sep="",end=" ")
		for k in div(l[i]):
			print(k,sep="",end=" ")
		print()
"""
