#!coding=utf-8
import sys, math, random

def main():
	n = 16
	minn = (1<<(n-1)) + 1
	maxn = (1<<n) - 1
	i = minn-2
	with open('./q3.middle', 'w') as f:
		while i < maxn+1:
			i = i + 2
			binval = dtobase(i, 2)
			f.write(binval + '\n')

def main2():
	print 'Case #1:'
	count = 50
	with open('./q3.middle') as f:
		for l in f:
			if test(l):
				count = count - 1
			if count <= 0:
				return

def test(binval):
	binval = binval.strip()
	ok = True
	factors = [binval]
	for j in range(2,11):
		val = basetod(binval, j)
		f = prime_test_miller_rabin(val, 50)
		if f == -1:
			return False
		factors.append(str(f))
	print ' '.join(factors)
	return True

def miller_rabin_witness(a, p):
    if p == 1:
        return False
    if p == 2:
        return True
 
    n = p - 1
    t = int(math.floor(math.log(n, 2)))
    u = 1
    while t > 0:
        u = n / 2**t
        if n % 2**t == 0 and u % 2 == 1:
            break
        t = t - 1
 
    b1 = b2 = compute_power(a, u, p)
    for i in range(1, t + 1):
        b2 = b1**2 % p
        if b2 == 1 and b1 != 1 and b1 != (p - 1):
            return False
        b1 = b2
    if b1 != 1:
        return False
 
    return True
 
def prime_test_miller_rabin(p, k):
    while k > 0:
        a = random.randint(1, p - 1)
        if not miller_rabin_witness(a, p):
        	r = 2
        	end = int(math.floor(math.sqrt(p)))
        	while r <= end:
        		if p % r == 0:
        			return r
        		r = r + 1
	        return -1
        k = k - 1
    return -1

def compute_power(a, p, m):
    result = 1
    p_bin = bin(p)[2:]
    length = len(p_bin)
    for i in range(0, length):
        result = result**2 % m
        if p_bin[i] == '1':
            result = result * a % m
 
    return result

def dtobase(n, base):
	s = []
	while n > 0:
		c = n % base
		s.append(str(c))
		n = n / base
	s.reverse()
	return ''.join(s)

def basetod(strs, base):
	s = 0
	for c in strs:
		s = s*base + ord(c) - ord('0')
	return s

if __name__ == '__main__':
	main()
	main2()