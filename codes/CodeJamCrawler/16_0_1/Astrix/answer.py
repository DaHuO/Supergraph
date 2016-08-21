

def calculate(N, case_num):
	global aout
	seen = set()

	if N == 0:
		aout.write('Case #{}: INSOMNIA\n'.format(case_num))
		return

	i = 1
	while len(seen) < 10:
		number = i * N
		for digit in str(number):
			seen.add(digit)
		i += 1

	aout.write('Case #{}: {}\n'.format(case_num, number))
	return

if __name__ == "__main__":
	doc = open('A-large.in', 'r')
	aout = open('aout.txt', 'w')

	cases = int(doc.readline())

	for i in range(1, cases+1):
		N = int(doc.readline())
		calculate(N, i)

	doc.close()
