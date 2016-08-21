
f = open('file')
lines = int(f.readline())

for j in range(0, lines):
	number = int(f.readline())
	if number == 0:
		print "Case #" + str(j + 1) + ": INSOMNIA"
		continue

	m = 0
	binary = 0
	while binary != 2**10 - 1:
		m = m + 1
		digits=str(m * number)
		for i in digits:
			binary = binary  | int(bin(2**int(i)), 2)

	print "Case #" + str(j + 1) + ": " + str(number * m)
