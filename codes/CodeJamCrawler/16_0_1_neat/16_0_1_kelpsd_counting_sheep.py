# first input T: # test cases
# each following input: N value
# 0 -> INSOMNIA

import sys

def count_sheep(n: int) -> int:
	if n == 0:
		return "INSOMNIA"
	else:
		digits = set()
		multiplier = 0
		while (len(digits) < 10):
			multiplier += 1
			for d in list(str(multiplier*n)):
				digits.add(d)
			# digits = digits.union(list(str(multiplier*n)))
		return multiplier*n


# assert(count_sheep(0) == -1)
# assert(count_sheep(1) == 10)
# assert(count_sheep(2) == 90)
# assert(count_sheep(11) == 110)
# assert(count_sheep(1692) == 5076)

t = int(sys.stdin.readline())

for i in range(0, t):
	n = int(sys.stdin.readline())
	print("Case #%d: %s" % (i+1, str(count_sheep(n))))








