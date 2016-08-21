def prime_gen():
	arch = open('primos.txt','w')
	arch.write('2 3 ')
	primos = [2,3]
	k_to_test = 6
	max_len = 1

	while len(str(primos[-1])) <= 16:
		t_es_primo = True

		t = k_to_test-1
		sqrt = t**0.5
		for p in primos:
			if t % p == 0:
				t_es_primo = False
				break
			if p > sqrt:
				break
		if t_es_primo:
			primos.append(t)
			arch.write('{0} '.format(t))

		t = k_to_test+1
		sqrt = t**0.5
		for p in primos:
			if t % p == 0:
				t_es_primo = False
				break
			if p > sqrt:
				break
		if t_es_primo:
			primos.append(t)
			arch.write('{0} '.format(t))
		k_to_test += 6

		if len(str(primos[-1])) > max_len:
			max_len = len(str(primos[-1]))
			print max_len

	arch.close()

def get_primos():
	arch = open('primos.txt')
	d = {}
	l = []
	for line in arch:
		line = line.strip().split()
		for i in line:
			d[int(i)] = True
			l.append(int(i))
	arch.close()
	return d,l

primos_d, primos_l = get_primos()

import random
def gen_coin(N):
	s = '1'
	for i in range(1,N-1):
		s += str(random.randrange(0,2))
	s += '1'
	return int(s)
#print gen_coin(5)
#print gen_coin(5)
#print gen_coin(5)
#x = gen_coin(5)

def coin2base(s,base):
	if base == 10:
		return s
	s = str(s)
	e = 0
	dec = 0
	while e < len(s):
		dec += int(s[-e-1])*base**e
		e += 1
	
	return dec

	num = ''
	while dec > 0:
		num = str(dec%base) + num
		dec /= base
	return int(num)

#print coin2base(x, 2)
#print coin2base(x, 3)
#print coin2base(x, 10)

def gencoins(N,J,primos_d,primos_l):
	j = 0
	print 'Case #1:'
	coins = []
	while j < J:
		coin = gen_coin(N)
		while coin in coins:
			coin = gen_coin(N)
		true_coin = False
		l_divs = []
		for i in range(2,11):
			c = coin2base(coin,i)
			found_p = False
			if c not in primos_d:
				for p in primos_l:
					if c % p == 0:
						l_divs.append(p)
						found_p = True
						break
					if c**0.5 < p:
						break
			if not found_p:
				break
		if len(l_divs) == 9:
			true_coin = True
		if true_coin:
			s = str(coin) + ' ' + ' '.join(map(str,l_divs))
			j = j+1
			print s
		coins.append(coin)
		

gencoins(32,500,primos_d,primos_l)