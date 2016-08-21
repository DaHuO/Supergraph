def all_check(num_dict):
	sum_of_values = 0
	for k, v in num_dict.items():
		sum_of_values = sum_of_values + k
	if sum_of_values == 45 and 0 in num_dict: return True
	else: return False

def count_sheep(n):
	cnt = 1
	num_dict = {}
	while cnt <= 1000:
		number, temp = cnt * n, cnt * n
		while number > 0:
			b = number % 10
			if b not in num_dict: num_dict[b] = 1
			number = number / 10
		if all_check(num_dict): return str(temp)
		cnt = cnt + 1
	return "INSOMNIA"

if __name__ == "__main__":
	t = int(raw_input())
	for i in range(1, t+1):
		n = int(raw_input())
		result = count_sheep(n)
		print "Case #%d: %s" %(i, result)
