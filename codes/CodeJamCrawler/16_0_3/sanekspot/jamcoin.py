n = 32
j = 500

def testcoin(binrepr):
	ans = []
	for base in xrange(2, 11):
		value = int(binrepr, base)
		divisorFound = False
		for divisor in xrange(2, 10000):
			if value % divisor == 0:
				divisorFound = True
				ans.append(str(divisor))
				break
		if not divisorFound:
			return None
	return ans
	
cur = 0
basecoin = (1 << (n - 1)) + 1
fout = open("output.txt", "w")
fout.write("Case #1:\n")
while j > 0:
	trycoin = basecoin + cur
	binrepr = "{0:b}".format(trycoin)
	prove = testcoin(binrepr)
	if prove:
		fout.write(binrepr + ' ')
		fout.write(' '.join(prove))
		fout.write('\n')
		#print binrepr, ' '.join([str(int(binrepr, base)) for base in xrange(2, 11)])
		j -= 1
	cur += 2