import os,sys,math

# Get a single item (int/string)
def get_item(flag):
	inp = raw_input()
	if flag == 0:
		return inp
	else:
		return int(inp)

# Get a tuple (int/string)
def get_tuple(flag):
	inp_tuple = get_list(flag)
	inp1 = inp_tuple[0]
	inp2 = inp_tuple[1]
	return inp1, inp2

# Get a list (int/string)
def get_list(flag):
	inp = raw_input()
	inp_list_str = inp.split()
	if flag == 0:
		return inp_list_str
	else:
		inp_list_int = []
		for inp_str in inp_list_str:
			inp_int = int(inp_str)
			inp_list_int.append(inp_int)
		return inp_list_int
	
# Get/Calculate/Fetch the output needed
def get_output(inp_word):
	last_word = inp_word[0]
	for i in range(1, len(inp_word)):
		char = inp_word[i]
		if char < last_word[0]:
			last_word = last_word + char
		else:
			last_word = char + last_word
	return last_word

# Main Function
def main():
	# Get no of test cases
	num_tests = get_item(1)

	for i in range(num_tests):
		inp_word = get_item(0)
		last_word = get_output(inp_word)
		print "Case #%d: %s" %(i+1, last_word)

# Starting Point
if __name__ == "__main__":
	main()
