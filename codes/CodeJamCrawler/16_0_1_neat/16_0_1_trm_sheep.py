from sys import argv

with open(argv[1]) as f:
	contents = [line for line in f]

contents = map(int, contents)

ALL_DIGITS = set(range(10))

def infinite_list(n):
	while True:
		yield n
		n += 1


def solve(num : int) -> str:
	last_num = 0
	n = num
	iterator = (x * n for x in infinite_list(2))
	chars = set()
	while True:
		if chars == ALL_DIGITS:
			return str(last_num)
		if num == last_num:
			return "INSOMNIA"
		chars = chars.union(set([int(n) for n in str(num)]))
		last_num = num
		num = next(iterator)

with open(argv[2], "w+") as f:
	contents = enumerate(contents)
	next(contents)
	for n, item in contents:
		f.write("Case #{}: {}\n".format(n, solve(item)))
