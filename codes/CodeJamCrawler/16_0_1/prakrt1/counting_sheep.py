__author__ = 'sony'

input_numbers = 0
seen_numbers = dict()
found_name = 0
OUT = open("output.txt", "w")


def read_from_file():
	fp = open('input.txt')
	return fp.readlines()


def start_counting_sheep():
	inp = read_from_file()
	global input_numbers, seen_numbers, OUT
	input_numbers = int(inp[0])

	for i in range(1, input_numbers + 1):
		current_number = int(inp[i])
		check_insomnia = am_in_insomnia(current_number)
		seen_numbers = dict()
		if check_insomnia:
			OUT.write("Case #%d: INSOMNIA\n" % i)
		else:
			name_next(current_number, 1)
			OUT.write("Case #%d: %d\n" % (i, found_name))


def name_next(name, multiplier):
	global found_name
	found_all = check_in_this_name(multiplier * name)
	if not found_all:
		name_next(name, multiplier + 1)
	else:
		found_name = multiplier * name


def check_in_this_name(name):
	global seen_numbers
	add_to_seen_bag(name)
	return True if len(seen_numbers.keys()) == 10 else False


def add_to_seen_bag(num):
	global seen_numbers
	while num != 0:
		seen_numbers[num % 10] = num % 10
		num /= 10


def am_in_insomnia(x):
	return True if x == 0 else False

start_counting_sheep()
