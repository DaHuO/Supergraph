import math
import time

# reject if all input digits odd or even
def pre_validate(n):
	return n != 0

def some_false(a):
	for x in a:
		if not x:
			return True
	return False

def counting_sheep(n):
	if not pre_validate(n):
		return "INSOMNIA"

	digits_seen = [False]*10
	a = 0
	while some_false(digits_seen):
		a += n
		for d_str in str(a):
			d = int(d_str)
			digits_seen[d] = True
		#time.sleep(0.1)
		#print(a)
		#print(digits_seen)
	return str(a)

def bulk_counting_sheep(inp_str):
	T = 0
	output_str = ""
	for i, line in enumerate(inp_str.splitlines()):
		if i == 0:
			T = int(line)
			continue

		line_result = counting_sheep(int(line))
		output_str += "Case #{}: {}\n".format(i, line_result)

	return output_str

with open("counting_sheep_input.txt", "r") as input_file:
	inp_str = input_file.read()
	out_str = bulk_counting_sheep(inp_str)
	with open("counting_sheep_output.txt", "w") as output_file:
		output_file.write(out_str)