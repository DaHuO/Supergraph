user_input = raw_input("Enter:")
user_input = raw_input().split(' ')
digits = int(user_input[0])
nums = int(user_input[1])

def convertBase(i,number):
	fnum = 0
	for j,c in enumerate(str(number)):
		fnum += int(i**(digits-j-1))*int(c)
	return fnum

def isPrime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def isJamCoin(n_base_2):
	if n_base_2[::-1][0] == '0':
		return False
	for j in range(2,11):
		cnum = convertBase(j,n_base_2)
		if isPrime(cnum):
			return False
	return True

def dividingFactor(n):
	if n % 2 == 0:
		return 2
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return x

def dividingFactors(n):
	dfArr = []
	for j in range(2,11):
		dfArr.append(dividingFactor(convertBase(j,n)))
	return dfArr

found = 0
l = 0
print "Case #1:"
while found < nums:
	low = (2**(digits-1)) + l
	base_2_num = "{0:b}".format(low)
	if len(base_2_num) > digits:
		break
	if isJamCoin(base_2_num):
		found += 1
		print str(base_2_num),
		alist = dividingFactors(base_2_num)
		print ' '.join(str(x) for x in alist)
	l += 1


