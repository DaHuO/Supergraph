from itertools import product
import math

def coinjam(N, J):
	#N: length of jam coin
	#J: Number of different jam coins
	list_sol = []
	a = [''.join(map(str, coin)) for coin in product([0, 1], repeat = N-2)]
	#List possible coins
	b = ['1'+i+'1' for i in a]
	l = len(b)
	#Count to J jam coins
	it = 0
	#return from isjamcoin function
	check = None
	for i in range(l):
		check = isjamcoin(b[i])
		if check != None:
			sol = b[i]+' '+check
			list_sol.append(sol)
			it +=1
		if it == J:
			break
	return '\n'.join(list_sol)


def isjamcoin(coin):
	nontrivial_divisors = []
	#Loop through base
	for i in range(2,11):
		t = base2int(coin, i)
		q = isNotPrime(t) 
		if q == None:
			return None
		else:
			nontrivial_divisors.append(q)
	if len(nontrivial_divisors)==9:
		return ' '.join(str(i) for i in nontrivial_divisors)
	return None

def isNotPrime(num):
	if num%2==0 and num>2:
		return 2
	for i in range(3, int(math.sqrt(num))+1,2):
		if num %i ==0:
			return i
	return None


def base2int(a, base):
	b = [int(i) for i in a]
	b.reverse()
	l = len(b)
	r = 0
	for i in range(l):
		r += b[i]* (base ** i)
	return r



def main():
	filename = 'C-small-attempt0.in'
	output = 'C-small-attempt0.out'
	f = open(filename,'r')
	#Output file
	out = open(output,'w')
	while True:
		line = f.readline()
		if line == '':
			break
		num_tests = int(line)
		for i in xrange(num_tests):
			line = f.readline().strip().split(' ')
			a = [int(j) for j in line]
			N,J = a
			sol = coinjam(N, J)
			s = 'Case #%s: ' %(i+1)
			s = s +'\n'+ sol
			out.write(s)
			out.write('\n')
		
if __name__ == "__main__":
	main()