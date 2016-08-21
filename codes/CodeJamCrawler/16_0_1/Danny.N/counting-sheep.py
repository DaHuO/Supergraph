def last_num(n):
	cur = 0
	seen_digits = {x:0 for x in range(10)}
	num_left = 10

	while num_left > 0:
		cur += n
		for d in str(cur):
			if seen_digits[int(d)] == 0:
				seen_digits[int(d)] = 1
				num_left -= 1
	return cur

num_cases = int(input())
for i in range(num_cases):
	N = int(input())
	if N == 0:
		print("Case #{}: INSOMNIA".format(i+1))
	else:
		print("Case #{}: {}".format(i +1,last_num(N)))