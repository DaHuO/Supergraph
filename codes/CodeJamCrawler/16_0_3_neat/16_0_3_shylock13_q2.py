import sys
import gmpy2
from gmpy2 import mpz

def find_factors(n):
    for i in range(2, 10000):
        div, mod = divmod(n, i)
        if not mod:
        	return i
    return 0

# string.txt
# n=32
# for i in range(0,100000):
# 	print '1'+'{0:b}'.format(i).zfill(n-2)+'1'
# exit()

#test.txt
zlimit = 501
print "Case #1:"
z = 0
for i in range(0,16384):
	n = raw_input()
	factors = []
	exclude = False
	for j in range( 2, 11 ):
		num = int(n,j)
		if gmpy2.is_prime( int( num ) ):
			exclude = True
			break
		else:
			if find_factors( int(num) ):
				factors.append( find_factors( int(num) ) )
			else:
				exclude = True
	if not exclude:
		z+=1
		if z==zlimit:
			break
		print n, " ".join([ str(k) for k in factors])
