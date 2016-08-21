import math

divisores=[0,0,0,0,0,0,0,0,0]
T = int(raw_input())
global j
j=0

def is_prime(n):
	if n%2==0 and n>2:
		return 2
	for i in range(3, int(math.sqrt(n))+1, 2):
		if n%i==0:
			return i
	return 0

def calc(v,i,dig,n):
	global j
	if j==0:
		return
	v[i]=dig
	if i>1:
		calc(v,i-1,0,n)
		calc(v,i-1,1,n)
		return
	prime=0
	for x in range(2,11):
		num=0
		pot=1
		for y in range(n-1,-1,-1):
			num+=v[y]*pot
			pot*=x
		
		#print(num)
		prime=is_prime(num)
		if prime==0:
			#print(num)
			break
		else:
			divisores[x-2]=prime
			#print(prime)
	if prime!=0:
		j-=1
		print(''.join(str(t) for t in v)),
		for z in divisores:
			print(str(z)),
		print

for t in range(T):
	raw=raw_input().split()
	n=int(raw[0])
	j=int(raw[1])
	
	v=[1]
	for i in range(n-2):
		v.append(0);
	v.append(1)
	
	print("Case #" + str(t+1) + ":")

	calc(v,n-2,0,n)
	calc(v,n-2,1,n)
