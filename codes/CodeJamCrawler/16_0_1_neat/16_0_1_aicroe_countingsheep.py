

def insertDigits(num, digits):
	if num == 0:
		digits[0] = True
	while num > 0:
		digits[num % 10] = True
		num = num / 10

def countNonFalses(vector):
	count = 0
	for b in vector:
		if b:
			count += 1
	return count

def sleepNumber(num):
	digits = [False for x in xrange(0, 10)]
	insertDigits(num, digits)
	step = 2
	while countNonFalses(digits) != 10:
		sleepNum = num* step
		insertDigits(sleepNum, digits)
		step += 1
	return sleepNum

#print sleepNumber(1)

if __name__ == '__main__':
	T = int(raw_input())
	for i in xrange(1, T + 1):
		num = int(raw_input())
		if num == 0:
			out = 'INSOMNIA'
		else:
			out = sleepNumber(num)
		print 'Case #{}: {}'.format(i, out)

