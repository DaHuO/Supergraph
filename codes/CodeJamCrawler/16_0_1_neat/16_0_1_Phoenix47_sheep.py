def count_sheep(n):
	num_set = set()
	i = 1
	last_n = n
	last_size = len(num_set)
	repeat_size_count = 0
	while (last_size != 10):
		last_n = i * n
		str_n = str(last_n)
		for c in str_n:
			num_set.add(c)
		if (last_size == len(num_set)):
			repeat_size_count += 1
		else:
			last_size = len(num_set)
			repeat_size_count=0
		if (repeat_size_count > 1000000):
			return "INSOMNIA"
		i += 1
	return last_n

if __name__ == "__main__":
	t = int(input())
	for i in range(1, t + 1):
		n = int(input())
		print("Case #{}: {}".format(i, count_sheep(n)))
