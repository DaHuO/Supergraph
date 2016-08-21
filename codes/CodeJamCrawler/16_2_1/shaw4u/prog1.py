#!/usr/bin/python
import sys
def remove(alphaBool,numStr):
	for x in numStr:
		alphaBool[ord(x) - ord('A')] = alphaBool[ord(x) - ord('A')] - 1

	return len(numStr)


T = int(raw_input())

for tcounter in range(1,T+1):
	s = str(raw_input())

	numBool = [0] * 10 
	alphaBool = [0] * 26

	for x in s:
		alphaBool[ord(x) - ord('A')] = alphaBool[ord(x) - ord('A')] + 1 
	
	count = len(s)

	while	alphaBool[ord('Z') - ord('A')] != 0:
			# this is zero
		remove(alphaBool,"ZERO")
		count = count - 4
		numBool[0] = numBool[0] + 1
	
	while alphaBool[ord('W') - ord('A')] != 0:
		remove(alphaBool,"TWO")
		count = count - 3
		numBool[2] = numBool[2] + 1
	
	while alphaBool[ord('U') - ord('A')] != 0:
		remove(alphaBool,"FOUR")
		count = count - 4
		numBool[4] = numBool[4] + 1

	while alphaBool[ord('X') - ord('A')] != 0:
		remove(alphaBool,"SIX")
		count = count - 3
		numBool[6] = numBool[6] + 1
	
	while alphaBool[ord('G') - ord('A')] != 0:
		remove(alphaBool,"EIGHT")
		count = count - 5 
		numBool[8] = numBool[8] +1
	
	while alphaBool[ord('F') - ord('A')] != 0:
		remove(alphaBool,"FIVE")
		count = count - 4
		numBool[5] = numBool[5] + 1 

	while alphaBool[ord('S') - ord('A')] != 0:
		remove(alphaBool,"SEVEN")
		count = count - 5
		numBool[7] = numBool[7] + 1
	
	while alphaBool[ord('O') - ord('A')] != 0:
		remove(alphaBool,'ONE')
		count = count - 3
		numBool[1] = numBool[1] + 1

	while alphaBool[ord('R') - ord('A')] != 0:
		remove(alphaBool,'THREE')
		count = count - 5
		numBool[3] = numBool[3] + 1
		
	while alphaBool[ord('I') - ord('A')] != 0:
		remove(alphaBool,'NINE')
		count = count - 4
		numBool[9] = numBool[9] + 1

	if count != 0:
		sys.stderr.write("anamoly")
		sys.stderr.write(s) 
	
	ans = ""
	for x in range(0,10):
		for y in range(0,numBool[x]):
			ans = ans +  str(x)
	
	print "Case #" + str(tcounter) + ": " + ans	


