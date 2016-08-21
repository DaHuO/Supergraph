def count_sheeps(value):
	latest = value
	valid = True
	digits = set()
	count = 1

	while len(digits) < 10 and valid:
		temp = latest
		latest = value * count

		if temp == latest and count != 1:
			valid = False

		for digit in list(str(latest)):
			digits.add(digit)
		count += 1		

	if valid:
		return latest
	else:
		return 'INSOMNIA'


def read_stdin():
	T = int(input())

	for t in range(T):
		value = int(input())
		print ("Case #%s: %s" % (t + 1, count_sheeps(value)))
		

read_stdin()