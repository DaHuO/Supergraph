#MAM, Google Code Jam - 2016 Qualification Round, Problem D
#Fractiles
#Trivial Solution

def solve(c):
	
	K, C, S = [int(x) for x in c.rstrip().split(" ")]

	return " ".join(str(e) for e in range(1, K+1))
	
def main():
	with open('D-small-attempt1.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			line = infile.readline()
			outfile.write("Case #" + str(x + 1) + ": " + str(solve(line)) + "\n")

if __name__ == "__main__":
	main()