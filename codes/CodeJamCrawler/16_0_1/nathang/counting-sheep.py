f = open('A-large.in.txt', 'r')
T = int(f.readline())

for t in range(0,T):
	N = int(f.readline()) # number chosen

	output = ''
	if N != 0:

		digits = [False] * 10
		prevNumber = N
		currentNumber = N
		factor = 2

		while True:

			# check to see if we are done
			done = True
			for d in digits:
				if d == False:
					done = False
					break
			if done:
				output = str(prevNumber)
				break

			# get the digits from the current number
			s = str(currentNumber)
			for c in s:
				i = int(c)
				digits[i] = True

			# increment the current number
			prevNumber = currentNumber
			currentNumber = N * factor
			factor += 1

	else:
		output = 'INSOMNIA'

	print('Case #' + str(t+1) + ': ' + output)
	
f.close()