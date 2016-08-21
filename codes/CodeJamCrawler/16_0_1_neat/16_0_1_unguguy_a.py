n = int(input())

for tc in range(1, n + 1):
	x = int(input())

	if x == 0:
		ans = "INSOMNIA"
	else:
		mult = 1
		digits = set()
		while True:
			y = x * mult
			digits.update([ch for ch in str(y)])
			if len(digits) == 10:
				ans = mult * x
				break
			mult += 1

	print("Case #{}: {}".format(tc, ans))