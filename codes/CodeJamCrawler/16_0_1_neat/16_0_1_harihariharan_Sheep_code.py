def extract_digit(number):
	str_num = str(number)
	digits = []
	for num in str_num:
		digits.append(int(num))
	return digits

def fetch_count(x):
	cur_iter = x
	digit_set = set()
	while True:
		digits = extract_digit(cur_iter)
		for digit in digits:
			digit_set.add(digit)
		if len(digit_set) == 10:
			return str(cur_iter)
		cur_iter += x
		if cur_iter == x:
			return "INSOMNIA"

if __name__ == "__main__":
	N = input()
	result = []
	for i in xrange(N):
		x = input()
		result.append(fetch_count(x))

	for i in xrange(N):
		print "Case #"+str(i+1)+": "+result[i]
