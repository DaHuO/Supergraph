from math import sqrt
from itertools import count, islice

def next_permu(L):
	n = len(L)
	if n == 0: return []
	if n == 1: return L
    
	i = n - 2
	while i >= 0:
		if L[i] < L[i+1]: break
		i -=1
    # All elements are larger than the right element
	if i < 0: return L[::-1]
    
	j = n - 1
	while L[j] <= L[i]:
		j -= 1
    # Switch i-th and j-th elements
	L[i], L[j] = L[j], L[i]
    # Reverse L[i+1:]
	L = L[:i+1] + L[i+1:][::-1]
	return L

'''def isPrime(n):
	if n < 2: return False
	for number in range(2,int(sqrt(n))+1):
		if n%number==0:
			return False
	return True
'''
def isPrime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True	
    
def factor(x):
	i=2
	while 1:
		#print i
		if(x==1 or x==i):
			i=i+1
			continue
		if ((x % i == 0)):
			return str(i)
		i=i+1
		
def testitbaby(t):
	countt=0
	n,j=map(int,raw_input().split())
	print "Case #"+str(t)+":"
	zero="0"*(n-2)
	for i in range(2**(n-2)):
		if(countt==j):
			break;
		factorlist=[]
		zero1=bin(i)[2:].rjust(n-2, '0')
		number=str(1)+str(zero1)+str(1)
		if not(isPrime(int(number,2)) or isPrime(int(number,3)) or isPrime(int(number,4)) or isPrime(int(number,4)) or isPrime(int(number,4)) or isPrime(int(number,5)) or isPrime(int(number,6)) or isPrime(int(number,7)) or isPrime(int(number,8)) or isPrime(int(number,9)) or isPrime(int(number,10))):
			countt=countt+1
			for k in range(2,11):
				factorlist.append(factor(int(number,k)));
			print number+' '+factorlist[0]+' '+factorlist[1]+' '+factorlist[2]+' '+factorlist[3]+' '+factorlist[4]+' '+factorlist[5]+' '+factorlist[6]+' '+factorlist[7]+' '+factorlist[8]
			del factorlist[:]
			
def main():
	test=int(raw_input());
	for t in range(1,test+1):
		testitbaby(t)
main()
