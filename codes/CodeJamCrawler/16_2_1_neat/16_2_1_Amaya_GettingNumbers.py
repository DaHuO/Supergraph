T = input();
tempT = T;
result = [];
while(T!=0):
	n = raw_input();
	List = []
	while(len(n)):
		if("Z" in n or "W" in n or "U" in n or "X" in n or "G" in n):
			if("Z" in n):
				n=n.replace("Z","",1);
				n=n.replace("E","",1);
				n=n.replace("R","",1);
				n=n.replace("O","",1);
				List.append(0);
			if("W" in n):
				n=n.replace("T","",1);
				n=n.replace("W","",1);
				n=n.replace("O","",1);
				List.append(2);
			if("U" in n):
				n=n.replace("F","",1);
				n=n.replace("O","",1);
				n=n.replace("U","",1);
				n=n.replace("R","",1);
				List.append(4);
			if("X" in n):
				n=n.replace("S","",1);
				n=n.replace("I","",1);
				n=n.replace("X","",1);
				List.append(6);
			if("G" in n):
				n=n.replace("E","",1);
				n=n.replace("I","",1);
				n=n.replace("G","",1);
				n=n.replace("H","",1);
				n=n.replace("T","",1);
				List.append(8);		
		elif("O" in n or "T" in n or "S" in n):
			if("O" in n):
				n=n.replace("O","",1);
				n=n.replace("N","",1);
				n=n.replace("E","",1);
				List.append(1);
			if("T" in n):
				n=n.replace("T","",1);
				n=n.replace("H","",1);
				n=n.replace("R","",1);
				n=n.replace("E","",1);
				n=n.replace("E","",1);
				List.append(3);
			if("S" in n):
				n=n.replace("S","",1);
				n=n.replace("E","",1);
				n=n.replace("V","",1);
				n=n.replace("E","",1);
				n=n.replace("N","",1);
				List.append(7);
		elif("V" in n):
			n=n.replace("F","",1);
			n=n.replace("I","",1);
			n=n.replace("V","",1);
			n=n.replace("E","",1);
			List.append(5);				
		else:
			n=n.replace("N","",1);
			n=n.replace("I","",1);
			n=n.replace("N","",1);
			n=n.replace("E","",1);
			List.append(9);
	List.sort();
	result.append("".join(str(x) for x in List));
	T=T-1;

i=0
while(i<tempT):   
    print "case #"+str(i+1)+":",result[i]
    i = i+1