def main():
	t = int(input())
	for i in range(t):
		x = int(input())
		print("Case #{}: {}".format(i+1, insonia(x)))

def insonia(x):
	if x == 0:
		return "INSOMNIA"
	i = 1
	num = x
	digit_set = set()
	digits(num, digit_set)
	while len(digit_set) < 10:
		i += 1
		num = x * i
		digits(num, digit_set)
	return num

def digits(num, digit_set):
	while num > 0:
		rest = num % 10
		num = num // 10
		digit_set.add(rest)

if __name__ == "__main__":
	main()