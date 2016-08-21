f = open("input3.txt")

noc = f.readline()

lenjc, noCoin = map(int,(f.readline()).split(' '))

no_of_digits = lenjc - 2
factor = []
middleDigits = '0' * no_of_digits
middleint = 0
okcoin = ''
coin = 1

def comp_for_each_base  (base, coin):
	bp = 0
	i = len(coin) - 1
	no = 0
	while i >= 0:
		tmp = int(coin[i])
		no += ((pow(base,bp)) * tmp)
		bp += 1
		i -= 1
	is_prime = primeCheck(no)
	if is_prime:
		return False
	else:
		return True

def primeCheck(no):
	is_prime = True
	if len(str(no)) > 6:
		d = no/2
		while d>1:
			if no%d == 0:
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
		if len(middleDigits) < no_of_digits:
			middleDigits = '%s%s' % ('0' * (no_of_digits - len(middleDigits)), middleDigits) 
		okcoin = '1' + middleDigits + '1'
		valid_coin = True
		for b in range(2, 11):
			valid_coin = comp_for_each_base  (b, okcoin)
			if not valid_coin:
				factor = []
				break
		if valid_coin:
			coin += 1
			got_coin = True
		middleint += 1
	print okcoin,' '.join(str(i) for i in factor)
	factor = []
		
