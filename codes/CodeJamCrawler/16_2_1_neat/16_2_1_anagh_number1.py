test=int(input())
for k in range(test):
	s=input()
	
	ans=[]
	
	while(s.find('Z')!=-1):
		s = s.replace("Z","",1)
		s = s.replace("E","",1)
		s = s.replace("R","",1)
		s = s.replace("O","",1)
		ans.append(0)
		
	while(s.find('X')!=-1):
		s = s.replace("S","",1)
		s = s.replace("I","",1)
		s = s.replace("X","",1)
		ans.append(6)
		
	while(s.find('W')!=-1):
		s = s.replace("T","",1)
		s = s.replace("W","",1)
		s = s.replace("O","",1)
		ans.append(2)
		
	while(s.find('U')!=-1):
		s = s.replace("F","",1)
		s = s.replace("O","",1)
		s = s.replace("U","",1)
		s = s.replace("R","",1)
		ans.append(4)
		
	while(s.find('S')!=-1):
		s = s.replace("S","",1)
		s = s.replace("E","",1)
		s = s.replace("V","",1)
		s = s.replace("E","",1)
		s = s.replace("N","",1)
		ans.append(7)
		
	while(s.find('O')!=-1):
		s = s.replace("O","",1)
		s = s.replace("N","",1)
		s = s.replace("E","",1)
		ans.append(1)
		
	while(s.find('N')!=-1):
		s = s.replace("N","",1)
		s = s.replace("I","",1)
		s = s.replace("N","",1)
		s = s.replace("E","",1)
		ans.append(9)
	
	while(s.find('V')!=-1):
		s = s.replace("F","",1)
		s = s.replace("I","",1)
		s = s.replace("V","",1)
		s = s.replace("E","",1)
		ans.append(5)
		
	while(s.find('R')!=-1):
		s = s.replace("T","",1)
		s = s.replace("H","",1)
		s = s.replace("R","",1)
		s = s.replace("E","",1)
		s = s.replace("E","",1)
		ans.append(3)
		
	while(s.find('H')!=-1):
		s = s.replace("E","",1)
		s = s.replace("I","",1)
		s = s.replace("G","",1)
		s = s.replace("H","",1)
		s = s.replace("T","",1)
		ans.append(8)
	
	ans.sort()
	
	ans=''.join(str(X) for X in ans)
	
	print("Case #"+str(k+1)+": "+ans)



