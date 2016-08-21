n = 32
j = 500

def first_divisor(n):
	d = 50
	tests = 0
	if (n % 3 == 0): return 3
	for i in range(5, int(n ** 0.5) + 1, 6):
		if n % i == 0: 
			return i
		if n % (i + 2) == 0:
			return i + 2
		tests += 2
		if tests >= d: return None

print("Case #1:")
for i in range(2 ** (n - 1) + 1, 2 ** n, 2):
	s = str(bin(i))[2:]
	divisors = []
	for base in range(2, 11):
		d = first_divisor(int(s, base))
		if d != None: divisors.append(d)
		else: break
	if len(divisors) == 9:
		print(s, " ".join(str(x) for x in divisors))
		j -= 1
		if j == 0: break
