# find longest contiguous
def find_longest_contig(input_str):
	cont_state = input_str[0]
	cont_index = -1 #index of last continguous char

	for char in input_str:
		if (char == cont_state):
			cont_index += 1
		else:
			break;
	return(cont_state, cont_index)


#

def flip(input_str, state, index):
	new_string = ''
	if (state == '+'):
		new_string = ((index + 1) * '-') + input_str[index + 1:]
	elif (state == '-'):
		new_string = ((index + 1) * '+') + input_str[index + 1:]

	return(new_string)

def complete(input_str):
	return True if (input_str == '+' * len(input_str)) else False


#print(find_longest_contig('+++-'))
#print(flip('+++-', '+', 2))
testcases = int(input())

for test in range(0,testcases):
	input_str = str(raw_input())
	flips = 0
	while (not complete(input_str)):
		(state, index) = find_longest_contig(input_str)
		input_str = flip(input_str, state, index)
		flips+=1

	print("Case #%d: %d" %(test + 1, flips))


