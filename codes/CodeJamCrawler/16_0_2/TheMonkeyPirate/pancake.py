n = int(input())
case = 0

while n:
	n -= 1
	case += 1
	stack = input()[::-1]
	last = '+'
	count = 0

	for i in range(len(stack)):
		if last != stack[i]:
			count += 1
		last = stack[i]

	print('Case #', case, ': ', count, sep='')