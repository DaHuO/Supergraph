""" Neely Fawaz
Google CodeJam

First, she picks a number N. Then she starts naming N, 2 * N, 3 * N, and so on.
Fall asleep after one of each digit
What is the last number that she will name before falling asleep?
If she will count forever, print INSOMNIA instead.

Input:
The first line of the input gives the number of test cases, T. 1 <= T <= 100.
T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen.
Small dataset: 0 <= N <= 200.  Large dataset: 0 <= N <= 10^6
Output:
For each test case, output one line containing Case #x: y, where x is the test case number
(starting from 1) and y is the last number that Bleatrix will name before falling asleep,
according to the rules described in the statement. 
"""

def count_sheep(N):
	""" Bleatrix keeps counting multipes of N until she has seen each digit once"""

	if N == 0:
		return "INSOMNIA"

	digits = [0 for x in range(0,10)]
	finished = False
	count = 1
	num = 0

	while not finished and count < 100:
		num = N * count
		num_digits = str(num)
		for i in range(len(num_digits)):
			digits[int(num_digits[i])] = 1
			pass
		digitsSeen = 0
		for x in digits:
			if x == 1:
				digitsSeen += 1
		if digitsSeen == 10:
			finished = True
		count += 1

	return num

T = raw_input()
for i in range(int(T)):
	print "Case #" + str(i+1) + ":",
	print count_sheep(int( raw_input() ))