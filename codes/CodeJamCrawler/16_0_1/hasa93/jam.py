
def solve(case, n):
	nums = [0] * 10
	counter = 1

	while sum(nums) != 10:

		if counter > 10**4:
			print 'Case #' + `case` + ": INSOMNIA"
			return

		s = str(n * counter)

		for i in s:
			nums[int(i)] = 1

		counter += 1

	print 'Case #' + `case` + ": " + `n * (counter - 1)`

def readInput(path):
	with open(path) as f:
		content = [int(line.rstrip('\n')) for line in f]

		for n in range(1, len(content)):
			solve(n, content[n])


#solve(0)
readInput('/home/hasa93/Downloads/A-large.in')