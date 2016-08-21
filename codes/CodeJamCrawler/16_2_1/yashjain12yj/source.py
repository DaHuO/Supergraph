for x in range(int(input())):
	s=input()
	a=[]
	print(s)
	while s!="":
		if ("Z" in s) and ("E" in s) and ("R" in s) and ("O" in s):
			a.append("0")
			s=s.replace('Z','')
			s=s.replace('E','')
			s=s.replace('R','')
			s=s.replace('O','')
		if ("O" in s) and ("N" in s) and ("E" in s):
			a.append("1")
			s=s.replace('O','')
			s=s.replace('N','')
			s=s.replace('E','')
		if ("T" in s) and ("W" in s) and ("O" in s):
			a.append("2")
			s=s.replace('T','')
			s=s.replace('W','')
			s=s.replace('O','')
		if ("T" in s) and ("E" in s) and ("R" in s) and ("H" in s) and (s.count("E")>=2):
			a.append("3")
			s=s.replace('T','')
			s=s.replace('E','')
			s=s.replace('R','')
			s=s.replace('H','')
			s=s.replace('E','')
		if ("F" in s) and ("R" in s) and ("O" in s) and ("U" in s):
			a.append("4")
			s=s.replace('F','')
			s=s.replace('O','')
			s=s.replace('U','')
			s=s.replace('R','')
		if ("F" in s) and ("I" in s) and ("V" in s) and ("E" in s):
			a.append("5")
			s=s.replace('F','')
			s=s.replace('I','')
			s=s.replace('V','')
			s=s.replace('E','')
		if ("S" in s) and ("I" in s) and ("X" in s):
			a.append("6")
			s=s.replace('S','')
			s=s.replace('I','')
			s=s.replace('X','')
		if ("S" in s) and ("E" in s) and ("V" in s) and (s.count("E")>=2) and ("N" in s):
			a.append("7")
			s=s.replace('S','')
			s=s.replace('E','')
			s=s.replace('V','')
			s=s.replace('E','')
			s=s.replace('N','')
		if ("E" in s) and ("I" in s) and ("G" in s) and ("H" in s) and ("T" in s):
			a.append("8")
			s=s.replace('E','')
			s=s.replace('I','')
			s=s.replace('G','')
			s=s.replace('H','')
			s=s.replace('T','')
		if ("N" in s) and ("I" in s) and ("N" in s) and ("E" in s) and (s.count("N")>=2):
			a.append("9")
			s=s.replace('N','')
			s=s.replace('I','')
			s=s.replace('N','')
			s=s.replace('E','')
	a.sort()
	print("Case #"+str(x+1)+": "+''.join(a))