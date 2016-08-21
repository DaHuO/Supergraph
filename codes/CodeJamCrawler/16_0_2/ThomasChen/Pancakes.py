# Change the format of string to "ababababa..."
def foo(string):
	resList = [string[0]]
	for x in range(1, len(string)):
		if string[x] != resList[-1]:
			resList.append(string[x])
	return "".join(resList)

with open("B-large.in") as readfile:
	with open ("output.txt", "w") as writefile:
		N  = int(readfile.readline())
		for x in range(N):
			string = readfile.readline().strip()
			newString = foo(string)
			# For "+-+-+....", if it ends with "-", result is the length of the string, else, result equals (length - 1)
			if newString[-1] == '+':
				writefile.write("Case #" + str(x+1) + ": " + str(len(newString)-1) + "\n")
			else:
				writefile.write("Case #" + str(x+1) + ": " + str(len(newString)) + "\n")