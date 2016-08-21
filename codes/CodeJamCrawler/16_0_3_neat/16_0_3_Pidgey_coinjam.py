import numpy as np
import sys 
import math 
import string
import random

def read_case(file_in):
	file_line = file.readline()
	A,B = file_line.split()	
	A = int(A)
	B = int(B)
	return A,B 

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, min(int(math.sqrt(n)),int(1e6)) + 1, 2):
        if n % i == 0:
            return False

    return True

def id_generator(size, chars=["0","1"]):
	return ''.join(random.choice(chars) for _ in range(size))

def nontriv_div(n):
	if n % 2 == 0 and n > 2: 
		return 2
	for i in range(3, min(int(math.sqrt(n)),int(1e6)) + 1, 2):
		if n % i == 0:
			return i

	return 0
		


file = open(sys.argv[1],'r+')
num_entries =  int(file.readline())
print "\nThe Number Of Entries: " + str(num_entries)

nonprime = []

N, J = read_case(file)
print "N, J =", N,J
print ""
count = 0
while count < J:
	tryi = "1"+id_generator(N-2)+"1"
	prime = False
	for base in range(2,11):
		nn = long(tryi,base)
	
	# find if prime for any base 
		if is_prime(nn) == True:
			prime = True
			break

	if prime == False:
		nonprime.append(tryi)
		count+=1
		print "done ", count 
print nonprime
ntdiv = np.zeros((J,9))
for i in range(J):
	for base in range(2,11):
		nn = long(nonprime[i],base)
		ntdiv[i,base-2] = nontriv_div(nn)

file.close()
ntdiv = ntdiv.astype('int64')
print ntdiv

file_out = open('output.out','wr')
string = 'Case #1:\n'
file_out.write(string)	
for i in range(J):
	string = '%s %s %s %s %s %s %s %s %s %s\n' % (nonprime[i],str(ntdiv[i,0]),
						    str(ntdiv[i,1]),str(ntdiv[i,2]),
						    str(ntdiv[i,3]),str(ntdiv[i,4]),
						    str(ntdiv[i,5]),str(ntdiv[i,6]),
						    str(ntdiv[i,7]),str(ntdiv[i,8]))
	print string
	file_out.write(string)	
file_out.close()
