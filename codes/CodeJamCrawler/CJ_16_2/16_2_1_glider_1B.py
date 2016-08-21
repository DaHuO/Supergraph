T = input()

k = 1
#d = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}

while(T):
	s = ''
	l = [0,0,0,0,0,0,0,0,0,0]
	S = raw_input()
	if("Z" in S):
		l[0] = S.count("Z")
	
	if("X" in S):
		l[6] = S.count("X")
	
	if("F" in S):
		if("U" in S):
			l[4] = S.count("U")
		
		l[5] = S.count("F") - l[4]
		
	
	if("W" in S):
		l[2] = S.count("W")
	
	if("G" in S):
		l[8] = S.count("G")

	if("S" in S):
		if(l[6] != S.count("S")):
			l[7] = S.count("S") - l[6]

	if("O" in S):
		if((l[0]+l[2]+l[4])!=S.count("O")):
			l[1] = S.count("O") - (l[0]+l[2]+l[4])

	if("I" in S):
		if((l[5]+l[6]+l[8])!=S.count("I")):
			l[9] = S.count("I") - (l[5]+l[6]+l[8])
	
	if("R" in S):
		if((l[0]+l[4])!=S.count("R")):
			l[3] = S.count("R") - (l[0]+l[4])

	'''
	if("N" in S):
		if("V" in S):
			if(l[5] != S.count("V")):
				l[7] = S.count("V") - l[5]
		if("I" in S):
			if(l[5] != S.count("I")):
				l[7] = S.count("I") - l[5]
		else:
			l[1] = S.count("N")
	if("H" in S):
		if(l[8] == 0):
			l[3] = S.count("H")
	'''
	for i in range(len(l)):
		j = ''
		if(l[i]>0):
			j = str(i)*l[i]
			s+=j
	
	print "Case #"+str(k)+": "+s
	k += 1
	T -= 1
