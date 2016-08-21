
import numpy as np
import math
import warnings
import string
warnings.filterwarnings('ignore')

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def smallestdivisor(n):
	"""returns the smallest non-trivial divisor of n"""
	d = 2 # to begin
	while n % d != 0:
		d = d+1
	return d

with open("A-large.in", "r") as f:
		
		T = int(f.readline().strip())

		for i in range(T):
			print ("Case #" + str(i+1) + ": ",end="")
			L = f.readline().split()
			ls = list(L[0])

			k=[]
			k.append(ls[0])
			for i in range (len(ls)-1):
				if (ls[i+1]>=k[0]):
					k.insert(0, ls[i+1])
				else:
					k.insert(len(k), ls[i+1])

			print (''.join(k))

			'''
			N=int(L[0])
			J=int(L[1])

			print ("Case #" + str(i+1) + ":\n",end="")
			st = 1 + pow(2,N-1)
			en = pow(2,N)-1

			n=0
			for i in range(st,en+1,2):

				if (n==J):
					break

				tmp = bin(i)
				tmp = tmp[2:]
				l=[]
				for base in range(2,11):
					tmp_2 = int(tmp,base)
					if ( is_prime(tmp_2)==True ):
						break
					else:
						l.append(smallestdivisor(tmp_2))

				if (len(l)==9):
					n=n+1
					print (str(tmp)+" ",end="")
					for p in range(9):
						print (str(l[p])+" ",end="")
					print ("")
				'''
