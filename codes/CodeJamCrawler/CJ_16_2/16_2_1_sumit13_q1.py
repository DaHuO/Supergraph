T = int(raw_input())

for t in range(1, T+1):
	arre = [0]*26
	arrm = [0]*10

	s = list(raw_input())
	
	for c in s:
		arre[ord(c) - ord('A')]+=1

	x = arre[ord('Z') - ord('A')]
	arre[ord('Z') - ord('A')] = 0
	arre[ord('R') - ord('A')] -= x
	arre[ord('O') - ord('A')] -= x
	arre[ord('E') - ord('A')] -= x
	arrm[0] += x
		
	x = arre[ord('W') - ord('A')]
	arre[ord('W') - ord('A')] = 0
	arre[ord('T') - ord('A')] -= x
	arre[ord('O') - ord('A')] -= x
	arrm[2] += x

	x = arre[ord('G') - ord('A')]
	arre[ord('G') - ord('A')] = 0
	arre[ord('E') - ord('A')] -= x
	arre[ord('I') - ord('A')] -= x
	arre[ord('H') - ord('A')] = 0
	arre[ord('T') - ord('A')] -= x
	arrm[8] += x

	x = arre[ord('X') - ord('A')]
	arre[ord('X') - ord('A')] = 0
	arre[ord('S') - ord('A')] -= x
	arre[ord('I') - ord('A')] -= x
	arrm[6] += x

	x = arre[ord('S') - ord('A')]
	arre[ord('E') - ord('A')] -= x
	arre[ord('S') - ord('A')] = 0
	arre[ord('V') - ord('A')] -= x
	arre[ord('E') - ord('A')] -= x
	arre[ord('N') - ord('A')] -= x
	arrm[7] += x

	x = arre[ord('V') - ord('A')]
	arre[ord('V') - ord('A')] = 0
	arre[ord('F') - ord('A')] -= x
	arre[ord('I') - ord('A')] -= x
	arre[ord('E') - ord('A')] -= x
	arrm[5] += x

	x = arre[ord('F') - ord('A')]
	arre[ord('F') - ord('A')] = 0
	arre[ord('O') - ord('A')] -= x
	arre[ord('U') - ord('A')] -= x
	arre[ord('R') - ord('A')] -= x
	arrm[4] += x

	x = arre[ord('O') - ord('A')]
	arre[ord('O') - ord('A')] = 0
	arre[ord('N') - ord('A')] -= x
	arre[ord('E') - ord('A')] -= x
	arrm[1] += x

	x = arre[ord('N') - ord('A')]
	arre[ord('N') - ord('A')] = 0
	arre[ord('I') - ord('A')] -= x/2
	arre[ord('E') - ord('A')] -= x/2
	arrm[9] += x/2

	x = arre[ord('T') - ord('A')]
	arre[ord('T') - ord('A')] = 0
	arre[ord('H') - ord('A')] -= x
	arre[ord('E') - ord('A')] -= 2*x
	arre[ord('R') - ord('A')] -= x
	arrm[3] += x

	outp = str("")
	for i in range(0, 10):
		for j in range(0, arrm[i]):
			outp = outp + str(i)

	print "Case #" + str(t) + ": " + outp