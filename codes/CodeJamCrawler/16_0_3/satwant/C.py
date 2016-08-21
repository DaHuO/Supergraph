def base(msk, b):
	ret = 0;
	_msk = msk
	pw = 1
	while msk > 0:
		dig = msk%2
		if dig: ret += pw
		pw *= b
		msk /= 2
	# print "Base: {0} {1}: {2}".format(_msk, b, ret)
	return ret

def factor(n):
	i = 2
	while i <= n/i:
		if n%i == 0: return i
		i += 1
	return n

def go(len, cnt):
	for msk in xrange(2**(len-2)):
		if cnt == 0: break
		num = (msk*2) + 1 + (2**(len-1))
		f = 1
		bases = [0]*11
		keys = [0]*11
		
		for i in xrange(2,11):
			bases[i] = base(num,i)
			fact = factor(bases[i])
			if fact == bases[i]:
				f = 0
				break
			else: keys[i] = fact

		if f:
			cnt -= 1

			print "{0} ".format(bases[10]),
			for i in xrange(2,11):
				print "{0} ".format(keys[i]),
			print ""

if __name__ == "__main__":
	tests = input()
	for test in xrange(1,tests+1):
		n, j = map(int, raw_input().split())
		print "Case #{0}:".format(test)
		go(n, j)