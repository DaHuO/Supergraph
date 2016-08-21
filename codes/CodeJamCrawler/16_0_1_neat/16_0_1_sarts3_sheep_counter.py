def check_last_number(num):
	if num == 0:
		return 'INSOMNIA'
	all_numbers = ['0','1','2','3','4','5','6','7','8','9']
	i = 1
	while True:
		result = num * i
		for number in str(result):
			if number in all_numbers:
				all_numbers.remove(number)
		if all_numbers:
			i += 1
		else:
			break

	return result


def handle_input():
	i = 1
	first_line = input()
	while i <= 100:
		print "Case #{}: {}".format(i, check_last_number(int(input())))
		i += 1


if __name__ == "__main__":
    handle_input()