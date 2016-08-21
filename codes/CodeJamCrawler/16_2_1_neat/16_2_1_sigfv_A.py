n = int(input())
for _ in range(n):
	red = [("Z", "ZERO", "0"), ("W", "TWO", "2"), ("X", "SIX", "6"), ("G", "EIGHT", "8"), ("H", "THREE", "3"), ("S", "SEVEN", "7"), ("V", "FIVE", "5"), ("F", "FOUR", "4"), ("I", "NINE", "9"), ("N", "ONE", "1")]
	d = {}
	numbers = ""
	s = input()
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	while True:
		found = False
		for p in red:
			if p[0] in d and d[p[0]] != 0:
				found = True
				for c in p[1]:
					d[c] -= 1
				numbers += p[2]
				break;
		if not found:
			break
	print("Case #" + str(_ + 1) + ":", "".join(sorted(numbers)))