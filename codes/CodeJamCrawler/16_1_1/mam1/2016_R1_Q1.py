#MAM, Google Code Jam - 2016 Round 1, Problem 1
#The Last Word

def solve(c):
	c = c.rstrip()

	answer = c[0]

	for ch in c[1:]:
		if ch >= answer[0]:
			answer = ch + answer
		else:
			answer = answer + ch

	return answer

def main():
	with open('A-large.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			line = infile.readline()
			outfile.write("Case #" + str(x + 1) + ": " + str(solve(line)) + "\n")

if __name__ == "__main__":
	main()