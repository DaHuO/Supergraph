
def solve(string):
	if len(string) == 1:
		if string == "+":
			return 0;
		else:
			return 1;
	if (string[1] == string[0]):
		return 0 + solve(string[1:])
	return 1 + solve(string[1:])

if __name__ == '__main__':
	cases = int(raw_input())
	for i in range(1,cases+1):
		print "Case #" + str(i) + ": " + str(solve(str(raw_input())))