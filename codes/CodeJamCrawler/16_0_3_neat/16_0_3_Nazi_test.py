

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats
from sklearn.cross_validation import KFold
from pylab import *
from sklearn import datasets, linear_model
import timeit
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


out = open('smallOut', 'w')
with open("C-small-attempt0.in", "r") as f:
		
		T = int(f.readline().strip())

		for i in range(T):
			
			L = f.readline().split()
			N=int(L[0])
			J=int(L[1])

			out.write("Case #" + str(i+1) + ":\n")

			n=0
			st = 1 + pow(2,N-1)
			en = pow(2,N)-1

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
					out.write(str(tmp)+" ")
					for p in range(9):
						out.write(str(l[p])+" ")
					out.write("\n")
				
