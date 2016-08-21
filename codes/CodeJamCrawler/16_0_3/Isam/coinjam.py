from math import sqrt; import itertools
from itertools import count, islice
import time

N = 15
Array1 = [''.join(seq) for seq in itertools.product('01', repeat=N)]
Array2 = [''.join(seq) for seq in itertools.product('01', repeat=N)]

def find_factors(x):
   for i in range(2, x):
       if x % i == 0:
           return i

#def isPrime(n):
#    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def isPrime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1

def construct(J):
	B = [[0 for j in range(11)] for i in range(J)]
	tmpB = [0 for i in range(11)]
	c = 0
	counter = 0
	pCounter = 0
	aCounter = 0
	while c < J:
		for it in Array2:
			tmpNum1 = Array1[aCounter]
			tmpNum2 = it
			#print('1'+tmpNum1+tmpNum2+'1')

			for i in range(2,11):
				tmpBaseNum = int('1'+tmpNum1+tmpNum2+'1',i)
				prime = isPrime(tmpBaseNum)
				if not prime:
					tmpB[i] = tmpBaseNum
					pCounter += 1
				else:
					break
			if pCounter == 9 and counter < J: 
				c += 1
				B[counter][1] = tmpBaseNum
				for g in range(2,11):
					B[counter][g] = find_factors(tmpB[g])
				counter += 1
			else:
				return B
			#print(counter)
			aCounter += 1
			pCounter = 0
	return B
			

if __name__ == '__main__':
	#print(construct(3))
	
	start_time = time.time()

	n = 32
	J = 500
	Ans = [[]]

	fOut = open('C-result-large.txt','w')

	Ans = construct(J)
	fOut.write('Case #'+'1'+':\n')

	for i in range(J):
		for j in range(1,11):
			fOut.write(str(Ans[i][j])+' ')
		fOut.write('\n')

	print('ends here')

	# checking ...
	'''
	lst = []
	b = []
	p = []

	for i in range(500):
		for j in range(500):
			if i != j:
				lst.append(Ans[i][1] == Ans[j][1])
	print(lst)

	for i in  range(500):
		for j in range(2,11):
			p.append(isPrime(Ans[i][j]))
			b.append(int(str(Ans[i][1]),j) % Ans[i][j] == 0)

	print('Divisor: '+str(False in b))
	print('Prime: '+str(False in p))
	'''

	print("--- %s seconds ---" % (time.time() - start_time))
	
	
