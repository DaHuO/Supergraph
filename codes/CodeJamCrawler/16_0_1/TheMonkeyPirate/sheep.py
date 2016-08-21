def main():
	n = int(input())

	if n == 0:
		return "INSOMNIA"

	val = 0
	used = [False] * 10

	while False in used:
		val += n
		strVal = str(val)

		for i in range(len(strVal)):
			used[int(strVal[i])] = True

	return val

n = int(input())
case = 0

while n:
	n -= 1
	case += 1

	print('Case #', case, ': ', main(), sep='');
