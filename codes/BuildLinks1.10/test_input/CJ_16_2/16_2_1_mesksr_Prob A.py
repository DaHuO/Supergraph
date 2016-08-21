for t in xrange(int(raw_input())):
	s = raw_input()
	count = [0]*100
	num = [0]*10
	for c in s:
		count[ord(c)]+=1
	
	count[2] = count[ord('W')]
	count[ord('T')] -= count[ord('W')]
	count[ord('O')] -= count[ord('W')]
	
	count[4] = count[ord('U')]
	count[ord('F')] -= count[ord('U')]
	count[ord('O')] -= count[ord('U')]
	count[ord('R')] -= count[ord('U')]
	
	count[6] = count[ord('X')]
	count[ord('S')] -= count[ord('X')]
	count[ord('I')] -= count[ord('X')]
	
	count[8] = count[ord('G')]
	count[ord('E')] -= count[ord('G')]
	count[ord('I')] -= count[ord('G')]
	count[ord('H')] -= count[ord('G')]
	count[ord('T')] -= count[ord('G')]
	
	count[0] = count[ord('Z')]
	count[ord('E')] -= count[ord('Z')]
	count[ord('O')] -= count[ord('Z')]
	count[ord('R')] -= count[ord('Z')]
	
	count[5] = count[ord('F')]
	count[ord('I')] -= count[ord('F')]
	count[ord('V')] -= count[ord('F')]
	count[ord('E')] -= count[ord('F')]
	
	count[1] = count[ord('O')]
	count[ord('N')] -= count[ord('O')]
	count[ord('E')] -= count[ord('O')]
	
	count[7] = count[ord('V')]
	count[ord('E')] -= count[ord('V')]
	count[ord('S')] -= count[ord('V')]
	count[ord('E')] -= count[ord('V')]
	count[ord('N')] -= count[ord('V')]
	
	count[3] = count[ord('T')]
	count[ord('H')] -= count[ord('T')]
	count[ord('R')] -= count[ord('T')]
	count[ord('E')] -= count[ord('T')]
	count[ord('E')] -= count[ord('T')]
	
	count[9] = count[ord('N')]
	
	ans = ""
	for i in range(10):
		ans += str(i)*count[i]
		
	print ans
	
	
	
	
