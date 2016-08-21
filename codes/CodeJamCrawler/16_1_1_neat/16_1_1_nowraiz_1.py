

def lastword(string):
	result = "";
	for i in string:
		if result == "":
			result += i;
		else:
			if (i >= result[0]):
				result = i + result;
			else:
				result = result + i;
	return result;


if __name__ == '__main__':
	cases = int(raw_input());
	for i in range(cases):
		print "Case #" + str(i+1) + ": " + lastword(str(raw_input()));
