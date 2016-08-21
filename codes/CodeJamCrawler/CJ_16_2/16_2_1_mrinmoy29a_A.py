f = open('A-large.in', 'r')
F  = open('A-large.out', 'w')
cases = 0

for line in f.readlines():
	if cases==0:
		tc = line
		cases+=1
		continue
		
	s = line
	ans = ''
	
	L1 = {'Z':'ZERO', 'W':'TWO', 'X':'SIX', 'G':'EIGTH'}
	L1digit = {'Z':'0', 'W':'2', 'X':'6', 'G':'8'}
	
	for letter in L1.keys():
		lcount = s.count(letter)
		ans += L1digit[letter] * lcount
		if lcount>0:
			for everyLetter in L1[letter]:
				s = s.replace(everyLetter, '', lcount)
	
	## Three
	lcount = s.count('T')
	ans += '3'*lcount
	if lcount>0:
		for everyLetter in 'THREE':
			s = s.replace(everyLetter, '', lcount)
	
	## Four
	lcount = s.count('R')
	ans += '4'*lcount
	if lcount>0:
		for everyLetter in 'FOUR':
			s = s.replace(everyLetter, '', lcount)
	
	## FIVE
	lcount = s.count('F')
	ans += '5'*lcount
	if lcount>0:
		for everyLetter in 'FIVE':
			s = s.replace(everyLetter, '', lcount)
	
	## Seven
	lcount = s.count('V')
	ans += '7'*lcount
	if lcount>0:
		for everyLetter in 'SEVEN':
			s = s.replace(everyLetter, '', lcount)
	
	## NINE
	lcount = s.count('I')
	ans += '9'*lcount
	if lcount>0:
		for everyLetter in 'NINE':
			s = s.replace(everyLetter, '', lcount)
	
	## ONE
	ans += '1'* (len(s)/3)
	
	ans = ''.join(sorted(ans))
	F.write('Case #' + str(cases) + ': ' + ans + '\n')
	cases += 1

f.close()
F.close()
	
