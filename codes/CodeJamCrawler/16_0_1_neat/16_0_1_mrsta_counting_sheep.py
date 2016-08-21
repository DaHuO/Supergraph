# counting_sheep.py
def test(n):

	x = 0

	if n == 0: return "INSOMNIA"

	d = [0,1,2,3,4,5,6,7,8,9]

	def isSleep():
		sleep = True
		for x in xrange(10):
			if d[x] != -1: sleep = False
		return sleep

	def dropDigits(digits):
		while  digits > 0:
			d[digits % 10] = -1
			digits /= 10

	while isSleep()==False:
		x += n
		dropDigits(x)

	return x

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
 	n = int(raw_input())
 	print "Case #{}: {}".format(i, test(n))
 	