T = int(input())
for i in range(T):
	N = int(input())

	if N == 0:
		output = "INSOMNIA"
	else:
		digits_left = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		mult = 1
		while True:
			for c in str(mult*(N)):
				if c in digits_left:
					digits_left.remove(c)
			
			if len(digits_left) == 0:
				output = (mult*(N))
				break
			mult += 1

	print("Case #%s: %s" % (i + 1, output))