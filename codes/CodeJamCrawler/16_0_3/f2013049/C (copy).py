import math
import itertools

def sieve(num):
	arr = [0 for a in range(num+1)]
	for a in range(2, num+1):
		if arr[a]==0:
			for b in range(a+a, num+1, a):
				arr[b] = 1
	return arr


test = int(raw_input())
for cs in range(test):
	num, j = [int(A) for A in raw_input().split()]
	for a in itertools.product(['0', '1'], repeat=num-2):
		string = '1'+''.join(a)+'1'
		prime_seq = []
		jhanda = 0
		for x in range(2, 11):
			numeral = int(string, base=x)
			prime = 0
			y = 3
			no = int(math.sqrt(numeral))
			while(y < no+1):
				if numeral%y==0:
					prime_seq.append(str(y))
					prime = 1
					break
				y+=2
			if (prime == 0):
				jhanda = 1
				break
		if jhanda == 0:
			j-=1
			print "Case #"+str(cs)+":\num",string, ' '.join(prime_seq)
			if j==0:
				break