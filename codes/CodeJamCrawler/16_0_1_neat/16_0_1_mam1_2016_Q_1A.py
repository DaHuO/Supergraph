#MAM, Google Code Jam - 2016 Qualification Round, Problem A
#Counting Sheep

def removeNumbers(n, nums):
	digits = [int(x) for x in str(n)]
	nums = [x for x in nums if x not in digits]
	return nums

def solve(c):
	
	theNumber= c.rstrip()
	theNumber= int(theNumber)

	if theNumber == 0: return "INSOMNIA"

	numbersLeft = range(10)
	originalNumber = theNumber
	x = 1

	while True:
		numbersLeft = removeNumbers(theNumber, numbersLeft)
		if not numbersLeft:
			break
		x = x + 1
		theNumber = originalNumber * x

	return theNumber

def main():
	with open('A-large.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			line = infile.readline()
			outfile.write("Case #" + str(x + 1) + ": " + str(solve(line)) + "\n")

if __name__ == "__main__":
	main()