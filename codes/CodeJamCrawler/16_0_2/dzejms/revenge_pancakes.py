t = int(input())
for i in range(1, t + 1):
	stack = str(raw_input())
	#print(stack)

	rev = stack[::-1]
	expect = '-'
	flips = 0
	for pos, char in enumerate(rev):
		if char != expect:
			continue
		flips += 1
		expect = '+' if expect == '-' else '-'

	print("Case #{}: {}".format(i, flips))


