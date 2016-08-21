def minFlip(string):
	count = 0
	for i in range(0, len(string) - 1):
		if string[i] != string[i + 1]:
			count += 1
	if string[-1] == '-':
		count += 1
	return count

if __name__ == "__main__":
    f = open('B-large.in', 'r')
    output = open('B-large.out', 'w')
    C = int(f.readline())
    for i in range(0, C):
        pancakesStr = f.readline().rstrip('\n')
        output.write("Case #" + str(i + 1) + ": " + str(minFlip(pancakesStr)) + "\n")