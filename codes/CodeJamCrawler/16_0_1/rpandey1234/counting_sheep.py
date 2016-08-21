import sys

def have_seen_all_digits(seen_numbers):
	return len(seen_numbers) == 10

def add_seen_digits(seen_numbers, num):
	while num > 0:
		seen_numbers.add(num % 10)
		num /= 10

def get_num_sheep(num):
	seen_numbers = set()
	# Special case for 0
	if num == 0:
		return 'INSOMNIA'
	current_num = num
	add_seen_digits(seen_numbers, current_num)
	while True:
		current_num += num
		add_seen_digits(seen_numbers, current_num)
		# print current_num, seen_numbers
		if have_seen_all_digits(seen_numbers):
			return current_num

def main(filename):
	# print "Reading from: ", filename
	with open(filename) as f:
		num_entries = int(f.readline())
		for i in range(num_entries):
			start_num = int(f.readline())
			# print start_num
			solution = get_num_sheep(start_num)
			print "Case #" + str((i + 1)) + ": " + str(solution)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "You should provide the input file name"
	else:
		main(sys.argv[1])
