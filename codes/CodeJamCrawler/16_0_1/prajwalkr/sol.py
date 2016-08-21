t = input()
for case in range(t):
	n = input()
	if n == 0:
		print "Case #{}: INSOMNIA".format(case + 1)
	else:
		digit = dict()
		i = 0
		while len(digit) != 10:
			i += n
			for x in list(str(i)):
				digit[x] = True
		print "Case #{}: {}".format(case + 1,i)
