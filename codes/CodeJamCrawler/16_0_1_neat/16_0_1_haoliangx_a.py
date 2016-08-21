all_digits = set("0123456789")

def solve(N):
	i = 0
	n = 0
	my_digits = set()
	while(my_digits != all_digits and i < 999999):
		i += 1
		n += N
		for c in str(n):
			my_digits.add(c)
	if my_digits == all_digits:
		return str(n)
	else:
		return "INSOMNIA"

items = []
n = int(raw_input())
for i in range(n):
	items.append(int(raw_input()))

i = 1
for item in items:
	print ("Case #%d: " % i) + solve(item)
	i += 1