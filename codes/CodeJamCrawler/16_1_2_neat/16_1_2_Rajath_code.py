import os,sys,math

# Get a single item (int/string)
def get_item(flag):
	inp = raw_input().strip()
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
	inp = raw_input().strip()
	inp_list_str = inp.split()
	if flag == 0:
		return inp_list_str
	else:
		inp_list_int = []
		for inp_str in inp_list_str:
			inp_str = inp_str.strip()
			inp_int = int(inp_str)
			inp_list_int.append(inp_int)
		return inp_list_int

# Get/Calculate/Fetch the output needed
def get_output(rows_cols, dim):
	miss = []
	heights = {}
	for i in range(len(rows_cols)):
		curr_list = rows_cols[i]
		for j in range(len(curr_list)):
			item = curr_list[j]
			if heights.get(item):
				heights[item] += 1
			else:
				heights[item] = 1

	count = 0
	for height in heights.keys():
		item = heights[height]
		if item%2 == 1:
			count += 1
			miss.append(height)
		if count == dim:
			break
	
	miss.sort()

	return miss

#Convert List to Str from Int
def convert_list(a):
	b = []
	for i in a:
		i = str(i)
		b.append(i)
	return b

# Main Function
def main():
	# Get no of test cases
	num_tests = get_item(1)

	for i in range(num_tests):
		dim = get_item(1)
		num = (2*dim)-1
		rows_cols = []
		for k in range(num):
			list = get_list(1)
			rows_cols.append(list)
			
		miss = get_output(rows_cols, dim)
		miss = convert_list(miss)
		miss = " ".join(miss)
		print "Case #%d: %s" %(i+1, miss)

# Starting Point
if __name__ == "__main__":
	main()
