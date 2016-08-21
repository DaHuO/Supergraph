from math import sqrt,pow
import time
from itertools import count, islice, product



def is_prime_fast(n):

	if n%2 == 0:
		return 2
	elif n%3 == 0:
		return 3
	i = 5
	while pow(i,2) <= n and i < 20: # i < 20 to save time 
		if n%i == 0:
			return  i
		elif n%(i+2) == 0:
			return i+2
		i += 6

	return 0

def is_prime(n):

	if n%2 == 0:
		return 2
	elif n%3 == 0:
		return 3
	i = 5
	while pow(i,2) <= n:
		if n%i == 0:
			return  i
		elif n%(i+2) == 0:
			return i+2
		i += 6

	return 0


def compute(list_s,flag):
	out_string = ""

	for i in range(2,11):
		n = 1
		sum_s = 0
		for x in reversed(list_s):
			if x != 0:
				sum_s += n
			n *= i
		if flag == 0:
			prime_check = is_prime_fast(sum_s)
		else:
			prime_check = is_prime(sum_s)
		if prime_check == 0:
			return 0;
		else:
			out_string = out_string + " " + str(prime_check)
	return out_string
       	
def write(n,j,f,flag):
	t2 = 0
	k = int(pow(2,n-1)) + 1
	while k < pow(2,n):
		list_s = [int(x) for x in bin(k)[2:]]
		if list_s[0] != 0 and list_s[n-1] != 0 and sum(list_s)%2 == 0:
			s = ''.join(str(x) for x in list_s)
			out_string = compute(list_s,flag)
			if out_string != 0:
				f.write(s + out_string + "\n")
				j -= 1
			if j==0:
				return 0
		k += 2		
	return 1


filename = "C-large.in"
f = open(filename, "r")
content = [x.strip('\n') for x in f.readlines()]
f.close()


# To start with we are only checking for prime factors less than 20 to save time. 
# If we don't get enough jamcoins (flag == 1) then we check for all prime factors.


f = open("output_C.out","w+")
flag = 0

for i,x in enumerate(content[1:]):
	f.write("Case #" + str(i+1) + ":\n")
	vari = content[i+1].split()
	n = int(vari[0])
	j = int(vari[1])
	flag = write(n,j,f,flag)

f.close()

if flag == 1:

	f = open("output_C.out","w+")

	for i,x in enumerate(content[1:]):
		f.write("Case #" + str(i+1) + ":\n")
		vari = content[i+1].split()
		n = int(vari[0])
		j = int(vari[1])
		write(n,j,f)

	f.close()







