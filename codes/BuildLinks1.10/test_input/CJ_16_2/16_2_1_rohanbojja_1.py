c=1
cases=input()
#	U		X		U		X		U		X		U		X		U
#l=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

#print l

while(c<=cases):
	s=raw_input()
	m=[]
	while(len(s)>0):
		if(s.find("Z")!=-1):
			s=s.replace("Z","",1)
			s=s.replace("E","",1)
			s=s.replace("R","",1)
			s=s.replace("O","",1)
			m.append(0)
		elif(s.find("W")!=-1):
			s=s.replace("T","",1)
			s=s.replace("W","",1)
			s=s.replace("O","",1)
			m.append(2)
		elif(s.find("U")!=-1):
			s=s.replace("F","",1)
			s=s.replace("O","",1)
			s=s.replace("U","",1)
			s=s.replace("R","",1)
			m.append(4)
		elif(s.find("X")!=-1):
			s=s.replace("S","",1)
			s=s.replace("I","",1)
			s=s.replace("X","",1)
			m.append(6)
		elif(s.find("G")!=-1):
			s=s.replace("E","",1)
			s=s.replace("I","",1)
			s=s.replace("G","",1)
			s=s.replace("H","",1)
			s=s.replace("T","",1)
			m.append(8)
		elif(s.find("O")!=-1):
			s=s.replace("O","",1)
			s=s.replace("N","",1)
			s=s.replace("E","",1)
			m.append(1)
		elif(s.find("R")!=-1):
			s=s.replace("T","",1)
			s=s.replace("H","",1)
			s=s.replace("R","",1)
			s=s.replace("E","",1)
			s=s.replace("E","",1)
			m.append(3)
		elif(s.find("F")!=-1):
			s=s.replace("F","",1)
			s=s.replace("I","",1)
			s=s.replace("V","",1)
			s=s.replace("E","",1)
			m.append(5)
		elif(s.find("S")!=-1):
			s=s.replace("S","",1)
			s=s.replace("E","",1)
			s=s.replace("V","",1)
			s=s.replace("E","",1)
			s=s.replace("N","",1)
			m.append(7)
		elif(s.find("N")!=-1):
			s=s.replace("N","",1)
			s=s.replace("I","",1)
			s=s.replace("N","",1)
			s=s.replace("E","",1)
			m.append(9)
	m.sort()	
	ans=""
	for x in m:
		ans=ans+str(x)
	print "Case #"+str(c)+": "+ans
	c=c+1