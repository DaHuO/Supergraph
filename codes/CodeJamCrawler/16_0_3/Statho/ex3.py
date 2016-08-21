import itertools

def is_prime(n):
	if n == 2 or n == 3:
		return -1
	if n < 2 or n % 2 == 0:
		return 2
	if n < 9:
		return -1
	if n % 3 == 0:
		return 3
	r = 10000
	div = 5
	while div <= r:
		if n % div == 0:
			return div
		if n % (div + 2) == 0:
			return div + 2
		div += 6
	return -1



inp = open('input.in', 'r')
out = open ('output3.out', 'w')

T = inp.readline().rstrip()
T = int(T)

for i in range(1, T + 1):
	x = inp.readline().split()

	it = itertools.count()

	count = 0
	out.write("Case #" + str(i)+":\n")
	for num in it:
		n = "%030d" % (int(bin(num)[2:]),)
		n = '1{0}1'.format(n)
		d = []
		for base in range(2, 11):
			acc = 0
			base2 = 1
			for index in range(-1, -(int(x[0]) + 1), -1):
				acc += int(n[index]) * base2
				base2 *= base
			q= is_prime(acc)
			if q > 0:
				d.append(q)
			else:
				break
		if (len(d)) == 9:
			out.write("{0} {1}\n".format(n, " ".join(map(str, d))))
			count += 1
		if count == int(x[1]):
			break 
			
out.close()
inp.close()
