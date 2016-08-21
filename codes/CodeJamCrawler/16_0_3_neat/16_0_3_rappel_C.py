from math import ceil
import time

start=time.time()

Len=16

def isPrime(n):
	if n<=2:
		return -1 if n==2 else 1
	for  i in range(2,ceil(n**.5)+1):
		if n%i==0:
			return i
	return -1

nums=[]
for i in range(2**(Len-1)+1, 2**Len):
	if i%2==0:
		continue
	x=isPrime(i)
	if x!=-1:
		nums.append([i,x])

nums=nums[:1000]

for b in range(3,11):
	i=0
	while i < len(nums):
		d=[int(nums[i][0]//2**j)%2 for j in range(Len)]
		n=0
		for k in range(Len):
			n+=d[k]*b**k
		x=isPrime(n)
		if x==-1:
			nums.pop(i)
		else:
			nums[i].append(x)
			i+=1

fout=open('c_small.out','w')

fout.write("case #1:\n")

for i in range(500):
	s=(str(bin(nums[i][0]))[2:])*2
	for j in range(9):
		s+=" "+str(nums[i][j+1])
	s+="\n"
	fout.write(s)

fout.close()