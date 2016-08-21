from math import *
 
	
def to_base(s, b):
	res = 0L
	for c in s:
		res = res * b + int(c)
	return res

	
inf = open("c.in", 'r')
outf = open("c.out", 'w')

t = int(inf.readline())

for tc in xrange(0, t):
	outf.write("Case #" + str(tc + 1) + ":\n")
	n, j = map(int, inf.readline().split())
	min_k = 1L
	for i in xrange(1, n / 2):
		min_k *= 2
	max_k = min_k * 2
	#print min_k, max_k, len(bin(min_k)[2:]), len(bin(max_k)[2:])
		
	jamcoins_counter = 0
	
	for k in xrange(min_k + 1, max_k, 2):
		binstrk = bin(k)[2:]
		outf.write(binstrk + binstrk + " " + str(k))
		for b in xrange(3, 11):				
			d = to_base(binstrk, b)
			outf.write(" " + str(d))
		outf.write("\n")
		jamcoins_counter += 1
		if (jamcoins_counter >= j):
			break
	
	 		
	
outf.close()		

