INPUT = "a.in"
OUTPUT = "a.out"


def solve(n):
	if n == 0:
		return "INSOMNIA"

	digits = [0]*10
	count = 0
	current = 0

	while count < 10:
		current += n
		temp = current

		while temp > 0:
			d = temp%10
			if digits[d] == 0:
				digits[d] = 1
				count += 1
			temp //= 10

	return str(current)

lines = [line.rstrip('\n') for line in open(INPUT)]
testNum = int(lines[0])
f = open(OUTPUT, 'w')
for i in range(testNum):
	t = int(lines[i+1])

	f.write("Case #%s: %s\n" % (i+1, solve(t)))

f.close()
