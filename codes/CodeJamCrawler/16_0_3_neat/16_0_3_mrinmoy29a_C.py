f = open("large.in", "r")
F = open("large.out", "w")

a = f.read().split('\n')
case = int(a[0])
n, J = (int(i) for i in a[1].split())
numbers = []
primes = []
length = 0

def create_prime(lim):
	num = 3
	
	for i in xrange(2, lim):
		numbers.append(1)
	
	length = len(numbers)
	
	for i in xrange(lim-2):
		if numbers[i]==1:
			primes.append(i+2)
			num = i+2
			k = i+num
			while k<length:
				numbers[k]=0
				k += num
	
	'''while num<=lim:
		for prime in primes:
			if prime*prime>num:
				primes.append(num)
				print num
				break
			if num%prime==0:
				break
		num+=1'''

create_prime( 10** ((n+1)/2) )
del numbers
F.write( 'Case #1:\n')

for coin in xrange(2**(n-1)+1, 2**n, 2):
	k = str( bin(coin))[2:]
	div = []
	flag = False
	
	for j in xrange(2, 11):
		num = int(k, j)
		for prime in primes:
			if prime*prime>num:
				flag = True
				break
			if num%prime==0:
				div.append( prime )
				break		
		if flag==True:
			break
	
	s = ''
	if flag==False:
		s+= str(k)
		s+= ' '
		for i in div:
			s+= str(i)
			s+= ' '
		s = s.lstrip(' ')
		s+= '\n'
		F.write(s)
		J-=1
	
	if J==0:
		break

f.close()
F.close()
