tests = int(input())

def get_result(number):
	s = set()
	if number == 0:
		return 'INSOMNIA'
	i = 1
	c = number
	while len(s) < 10:
		c = number * i
		i += 1
		s.update(str(c))
	return str(c)



for test in range(1, tests + 1):
	number = int(input())
	print('Case #%d: %s' % (test, get_result(number)))