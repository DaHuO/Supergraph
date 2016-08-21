t = int(raw_input())

for i in range(1, t+1):
	n = [int(s) for s in raw_input().split(" ")]

	num = []
	a = n[0]

	for j in range(10000):
		if len(num) == 10:
			break
		else:
			digits = list(set(list(str(a))))
			num += filter(lambda x: x not in num, digits)
			a += n[0]

	if len(num) != 10:
		a = "INSOMNIA"
	else:
		a -= n[0]

	print "Case #{}: {}".format(i, a)