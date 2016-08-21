from math import sqrt
from itertools import *
import itertools
import sys
primes=[]
inp=[]
def isPrime1(n):
     return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


test=input()
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
while(test):
	nums=raw_input().split()
	for x in nums:
		inp.append(int(x))

	cnt=0
	N=inp[0]
	J=inp[1]
	# ["".join(seq) for seq in itertools.product("01", repeat=3)]
	print 'Case #'+str(test)+':'
	interseq=["".join(seq) for seq in itertools.product("01", repeat=N-2)]
	for  x in interseq:
		string='1'
		string+=x
		string+='1'
		#string cal
		#dec no cal
		if cnt==J:
					break
	
		dec=[]
		for x in range(2,11):
			dec.append(int(string,x))
		
		
		#print primes
		k=0
		for x in dec:
			if (isPrime1(x)==False):
				k+=1

		
		if k==9:
			print string,
			for x in dec:
				fa=factors(x)

				fa.remove(1)
				fa.remove(x)
				print next(iter(fa)),
			cnt+=1
			print 
			

	if cnt==J:
					break
