def bleatrix_sleep(n):
	"""
	Function that takes in a number and determines whether bleatrix
	will sleep at a number or not

	:param n: Number bleatrix thinks of 
	"return m: Number bleatrix sleeps on, or INSOMNIA (string)
	"""
	seen = []
	all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	if n == 0:
		return 'INSOMNIA'
	else:
		i = 1
		while (seen != all_digits):
			m = n * i
			seen.extend([a for a in str(n * i)])
			seen = sorted(list(set(seen)))
			# print(seen)
			i = i + 1

		return (str(m))

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
m = []
for i in xrange(1, t + 1):
  m .append(int(raw_input()))  # read a list of integers, 2 in this case

for i, num in enumerate(m):
	print ("Case #" + str(i+1) + ": " + bleatrix_sleep(num)) 