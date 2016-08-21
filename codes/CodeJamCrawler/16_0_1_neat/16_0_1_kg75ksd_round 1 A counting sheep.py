# http://stackoverflow.com/a/975039
def get_digits(n):
	if n < 0: n = -n
	result = set()
	while n != 0:
		digit = n % 10
		result.add(digit)
		n //= 10
	return result

def solve(test):
	n = int(test)
	if n == 0:
		return 'INSOMNIA'
	else:
		encountered_digits = get_digits(n)
		all_digits = set([0,1,2,3,4,5,6,7,8,9])
		a = n
		while encountered_digits != all_digits:
			a += n
			encountered_digits.update(get_digits(a))
		return str(a)

def run(solve):
	t = int(input())
	for i in range(1, t + 1):
	  print("Case #{}: {}".format(i, solve(input())))	

run(solve)