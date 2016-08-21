import sys

def flip(x, list):
	for i in range(0, x + 1):
		if list[i] == "-":
			list[i] = "+"
		else:
			list[i] = "-"
	return list

def getLastIndexOfN(list):
	for i in range(len(list), 0, -1):
		if list[i - 1] == "-":
			return i - 1
	
	return -1
	
if __name__ == "__main__":

	tests = int(sys.stdin.readline())
	
	for test in range(1, tests + 1):
		s = sys.stdin.readline().replace("\n", "")
		s = [i for i in s]
		ans = 0
		while "-" in s:
			ans += 1
			s = flip(getLastIndexOfN(s), s)
			
		print ("Case #" + str(test) + ": " + str(ans))
