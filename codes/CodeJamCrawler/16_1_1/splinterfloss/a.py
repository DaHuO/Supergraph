import io_helper
def a(str):
	new_str = ""
	for i in xrange(0, len(str)):
		char = str[i]
		if i == 0:
			new_str = new_str + str[i]
		else:
			if str[i] < new_str[0]:
				new_str = new_str + str[i]
			else:
				new_str = str[i] + new_str
	return new_str.strip()

testCases = io_helper.get_input()
numCases = testCases[0]
testCases.pop(0)

io_helper.prep_output()

for i in xrange(0, len(testCases)):
	io_helper.write_output(i, a(testCases[i]))