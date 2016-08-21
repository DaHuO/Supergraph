from collections import defaultdict

def all_digits(num):
	while num > 0:
		yield num % 10
		num = num // 10

def find_last(x):
	if x == 0:
		return "INSOMNIA"

	dig_map = defaultdict()

	current_num = x

	while len(dig_map) != 10:
		
		for digit in all_digits(current_num):
			dig_map[digit] = True

		current_num = current_num + x

	return current_num - x 

def main():
	cases = int(input())
	counter = 0

	while counter < cases:
		counter = counter + 1
		x = int(input())
		print("Case #{x}: {y}".format(x=counter, y=find_last(x)))

main()