import math
def is_not_prime(n):
	l = [2,3,5,7,11]
	for i in range(0,5):
		if n % l[i] == 0:
			return l[i]
	return -1

def is_jamcoin(s):
	l = []
		
	for i in range (2, 11):
		v = is_not_prime(int(s , i))
		if v != -1 :
			l.append(v)
		else:
			return False, None

	return True, l	

def generate(n, j):
	srt = pow(2, n-1)+1
	end = pow(2, n)-1
	l = []
	c = 0
	
	for i in range (srt, end+1, 2):
		s = bin(i)
		s = s.replace('b' , '0')
		p,q = is_jamcoin(s)
		if p :
			print(int(s), end = ' ')
			for v in q:
				print(v, end = ' ')
			print('')
			c = c+1
			
			if c == j:
				return
	
	
		
k = int(input())
for i in range (0, k):
	n, j = map(int, input().split())
	print("Case #%d:" % (i+1))
	generate(n,j)
	
