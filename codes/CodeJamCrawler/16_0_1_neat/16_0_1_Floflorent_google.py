import sys

with open(sys.argv[1]) as f:
	content = f.readlines()
cases = int(content[0])

for x in xrange(1,cases + 1):
	digits = [False] * 10
	stop = 0
	i = 2
	original = int(content[x])
	number = original

	if number == 0:
		print "Case #" + str(x) + ": INSOMNIA"
	else:
		while stop == 0:
			stop = 1
			for n in xrange(0,10):
				if str(n) in str(number):
					digits[n] = True
			for n in digits:
				if n == False:
					stop = 0
			number = original * i
			i += 1
		print "Case #" + str(x) + ": " + str(number - original)

