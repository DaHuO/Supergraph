import sys

def reverse_stack(a, i):
	""" Flips the elements of a at i
	"""
	b = a[0:i+1]
	b.reverse()
	for i in range(len(b)):
		b[i] *= -1
	a[0:i+1] = b

	return a

def main(fin, fout):
	T = int(fin.readline())
	for t in range(T):
		input = fin.readline().strip()
		# print input
		stack = [0] * len(input)
		N = len(input)
		for i in range(N):
			if input[i] == '-':
				stack[i] = -1
			if input[i] == '+':
				stack[i] = 1
		# print stack
		answer = 0
		for i in reversed(range(N)):
			# print "element %d: %d" % (i, stack[i])
			if stack[i] == -1:
				# print "before:"
				# print stack
				# Check if top is also negative
				i_tempt = 0
				if stack[0] == 1:
					while stack[i_tempt] == 1:
						i_tempt += 1
					# "before pre flip:"
					# print stack
					stack = reverse_stack(stack, i_tempt-1)
					# "after pre flip:"
					# print stack
					answer += 1
				stack = reverse_stack(stack, i)
				# print "after:"
				# print stack
				answer += 1

		fout.write("Case #%d: %d\n" % (t+1, answer))
		print "Case #%d: %d\n" % (t+1, answer)
	return

if __name__ == '__main__':
	fin = open(sys.argv[1], "r")
	fout = open(sys.argv[2], "w")
	main(fin, fout)
