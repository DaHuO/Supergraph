#! usr/bin/python

f = open("C-large.in")

noc = f.readline()

lenOfJamCoin, noCoin = map(int,(f.readline()).split(' '))

noOfDigits = lenOfJamCoin - 2
factor = []
middleDigits = '0' * noOfDigits
middleint = 0
oriCoin = ''
coin = 1

def computeForBase(base, coin):
	#print 'check 4 base %d' % base
	basePower = 0
	i = len(coin) - 1
	no = 0
	#print 'check for base %d' % base
	while i >= 0:
		tmp = int(coin[i])
		no += ((pow(base, basePower)) * tmp)
		#coin = coin/10
		basePower += 1
		i -= 1
	#while coin:
		#tmp = coin % 10
		#no += ((pow(base, basePower)) * tmp)
		#coin = coin/10
		#basePower += 1
	is_prime = primeCheck(no)
	#print 'no is %d and it is prime?' % no
	#print is_prime
	#return coin is valid / not
	if is_prime:
		return False
	else:
		return True

def primeCheck(no):
	#print 'Check if %d is prime' % no
	is_prime = True
	#print 'no is %d and len is %d' % (no, len(str(no)) )
	if len(str(no)) > 6:
		d = no/2
		while d>1:
			if no%d == 0:
				#print 'by %d' % d
				if d in factor:
					d = d/2
				else:
					factor.append(d)
					return False
			else:
				d = d/2
		return True
	else:
		for i in range(2, no):
			if no%i == 0:
				if i in factor:
					d = d/2
				else:
					factor.append(i)
					is_prime = False
					break
		return is_prime

print "Case #1:"

while coin <= noCoin:
	got_coin = False
	while not got_coin:
		middleDigits = (bin(middleint)).replace('0b','')
		if len(middleDigits) < noOfDigits:
			middleDigits = '%s%s' % ('0' * (noOfDigits - len(middleDigits)), middleDigits) 
		oriCoin = '1' + middleDigits + '1'
		valid_coin = True
		#print 'checking coin - '+ oriCoin
		for b in range(2, 11):
			#print 'check %s' % oriCoin
			valid_coin = computeForBase(b, oriCoin)
			if not valid_coin:
				factor = []
				break
		if valid_coin:
			coin += 1
			got_coin = True
		middleint += 1
	fact = ' '.join(str(n) for n in factor)
	print oriCoin + ' ' + fact
	factor = []
		
