import math
import itertools as it

#http://stackoverflow.com/questions/18833759/python-prime-number-checker
def is_prime(n):
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

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

with open("output2.txt", "w") as out:
	num = 16
	n = 50
	r = [[1,0],[0,1]]*8
	lista = []

	out.write("Case #1:\n")
	cont = 0
	for item in it.product(*r):
		print('1')
		if item[0] == 1 and item[len(item)-1] == 1:
			soma = []
			for i in range(2,11):
				somap = 0
				j = len(item)-1
				for ind in item:
					if ind == 1:
						somap += ind*(i**j)
					j -= 1

				if somap == 0:
					break
				if is_prime(somap):
					break

				soma.append(somap)

			if len(soma) == 9:
				final = []
				for s in soma:
					for r in range(2,s-1):
						if s%r == 0:
							final.append(r)
							print(soma)
							print('final',final)
							break
				print('2')
				if len(final) == 9:
					f = ''
					for u in final:
						f += str(u)
						f += ' '
					h = ''
					for e in item:
						h += str(e)
					if not h in lista:
						lista.append(h)
						out.write("{0} {1}\n".format(h,f))

						cont +=1
						print('3')
					if cont == n:
						break

