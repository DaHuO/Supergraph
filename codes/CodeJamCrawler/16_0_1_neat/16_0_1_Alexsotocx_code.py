# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
global digits
digits = 0
def splitDigits(n):
	global digits
	#print("Digits Done = {}".format(digits))
	
	while n >= 10:
		d = int(n % 10)
		#print("Digit = {}".format(d))
		#print("N = {} {}".format(n, type(digits).__name__))
		n //= 10
		digits = (digits | (1 << d))

	digits = (digits | (1 << n))


t = int(input())  # read a line with a single integer
maxNumber = ((1 << 10) - 1)
for i in range(1, t + 1):
	digits = 0
	n = int(input())
	if n == 0:
		print("Case #{}: {}".format(i, "INSOMNIA"))
	else:		
		j = 1
		while digits != maxNumber:
			splitDigits(n * j)
			j += 1
		j-= 1
		print("Case #{}: {}".format(i, n*j))


	# check out .format's specification for more formatting options