T = int(raw_input())
for i in range(T):
	S = raw_input()
	counts = [0] * 26
	a = ord('A')
	for j in S:
		temp = ord(j) - a
		counts[temp] += 1
	
	ans = []
	if 'Z' in S:
		temp = counts[ord('Z') - ord('A')]
		for j in range(temp):
			# ans += "0"
			ans.append('0')
			counts[ord('Z') - ord('A')] -= 1
			counts[ord('E') - ord('A')] -= 1
			counts[ord('R') - ord('A')] -= 1
			counts[ord('O') - ord('A')] -= 1

	if 'W' in S:
		temp = counts[ord('W') - ord('A')]
		for j in range(temp):
			# ans += "2"
			ans.append('2')
			counts[ord('T') - ord('A')] -= 1
			counts[ord('W') - ord('A')] -= 1
			counts[ord('O') - ord('A')] -= 1
	
	if 'U' in S:
		temp = counts[ord('U') - ord('A')]
		for j in range(temp):
			# ans += "4"
			ans.append('4')
			counts[ord('F') - ord('A')] -= 1
			counts[ord('O') - ord('A')] -= 1
			counts[ord('U') - ord('A')] -= 1
			counts[ord('R') - ord('A')] -= 1
	
	if 'X' in S:
		temp = counts[ord('X') - ord('A')]
		for j in range(temp):
			# ans += "6"
			ans.append('6')
			counts[ord('S') - ord('A')] -= 1
			counts[ord('I') - ord('A')] -= 1
			counts[ord('X') - ord('A')] -= 1
	
	if 'G' in S:
		temp = counts[ord('G') - ord('A')]
		for j in range(temp):
			# ans += "8"
			ans.append('8')
			counts[ord('E') - ord('A')] -= 1
			counts[ord('I') - ord('A')] -= 1
			counts[ord('G') - ord('A')] -= 1
			counts[ord('H') - ord('A')] -= 1
			counts[ord('T') - ord('A')] -= 1
	
	if 'O' in S:
		temp = counts[ord('O') - ord('A')]
		for j in range(temp):
			# ans += "1"
			ans.append('1')
			counts[ord('O') - ord('A')] -= 1
			counts[ord('N') - ord('A')] -= 1
			counts[ord('E') - ord('A')] -= 1

	if 'H' in S:
		temp = counts[ord('H') - ord('A')]
		for j in range(temp):
			# ans += "3"
			ans.append('3')
			counts[ord('T') - ord('A')] -= 1
			counts[ord('H') - ord('A')] -= 1
			counts[ord('R') - ord('A')] -= 1
			counts[ord('E') - ord('A')] -= 2
	
	if 'F' in S:
		temp = counts[ord('F') - ord('A')]
		for j in range(temp):
			# ans += "5"
			ans.append('5')
			counts[ord('F') - ord('A')] -= 1
			counts[ord('I') - ord('A')] -= 1
			counts[ord('V') - ord('A')] -= 1
			counts[ord('E') - ord('A')] -= 1
	
	if 'S' in S:
		temp = counts[ord('S') - ord('A')]
		for j in range(temp):
			# ans += "7"
			ans.append('7')
			counts[ord('S') - ord('A')] -= 1
			counts[ord('E') - ord('A')] -= 2
			counts[ord('V') - ord('A')] -= 1
			counts[ord('N') - ord('A')] -= 1

	if 'I' in S:
		temp = counts[ord('I') - ord('A')]
		for j in range(temp):
			# ans += "9"
			ans.append('9')
			counts[ord('N') - ord('A')] -= 2
			counts[ord('I') - ord('A')] -= 1
			counts[ord('E') - ord('A')] -= 1

	ans.sort()
	print "Case #%d:" % (i+1),
	print ''.join(ans)