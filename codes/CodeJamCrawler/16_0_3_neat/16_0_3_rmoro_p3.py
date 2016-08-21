###
## Robert Morouney
## moro1422@mylaurier.ca
## Friday April 08 2016
##
## Google_Code Jam Qualify_C: Coin Jam
##
import math

fin = open('C-large.in', 'r')
fout = open('C-large.out','w')

def isprime(n):
	if n%2 == 0: return 2
	sqrt_n = math.sqrt(n)
	i = 3
	while i <= 50000:
		if n%i == 0: return i
		i += 2
	return 0

cases = 0
case = 0
for line in fin:
	if cases == 0: cases = int(line.strip())
	elif case >= cases: break
	else:
		case += 1
		fout.write("Case #{0}:\n".format(case))
		
		tmp = line.split(" ")
		N = int(tmp[0])
		J = int(tmp[1])
		##################################################
		lines_written = 0 
		num = 2**(N-1) + 1
		while num < (2**N)-1 and lines_written<J:
			temp = bin(num)[2:]
			pstring = temp + ' '
			ret = 0
			for i in range(2, 11):
				ret = isprime(int(temp,i))
				if ret == 0: break
				else: pstring = pstring + str(int(temp,i)/ret) + ' '
			if ret != 0: 
				fout.write(pstring[:-1] + '\n')
				lines_written += 1
			num += 2
					
