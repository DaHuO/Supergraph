import math
def asleep(n):
	i = 0
	num = n
	counter =  {'0': False,
				'1': False,
				'2': False,
				'3': False,
				'4': False,
				'5': False,
				'6': False,
				'7': False,
				'8': False,
				'9': False}
	while (False in counter.values() and i<=100):
		for digit in list(str(num)):
			counter[digit] = True
		i = i + 1
		num = (i+1) * int(n)
	return counter, (num - int(n))


t = int(raw_input())

for i in xrange(1, t + 1):
	number = int(raw_input())
	result = asleep(number)
	if (result[1] != 0):
		print 'Case #{}: {}'.format(i, result[1])
	else:
		print 'Case #{}: INSOMNIA'.format(i)