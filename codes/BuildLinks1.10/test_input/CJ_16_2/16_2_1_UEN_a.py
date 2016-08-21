import sys
import math

N = list()
CHAR = list()
DIGITS = ["ZERO",'ONE','TWO','THREE','FOUR','FIVE',"SIX","SEVEN","EIGHT","NINE"]

with open("A-large.in") as f :
#with open("A-small-attempt1.in") as f :
#with open("input.txt") as f :
	T = int(f.readline());
	for line in f :
		N.append([str(x) for x in line.split()]);

for l in N :
	for s in l :
		tmp = list()
		for c in s :
			tmp.append(c)
		CHAR.append(tmp)

#print (T)
#print (CHAR)
with open("A-large.txt", 'w') as f :
#with open("A-samll.txt", 'w') as f :
#with open("output.txt", 'w') as f :
	for tc in range(1, T+1) :
		
		data = "Case #%d: " % (tc)
		result = ""
		f.write(data)
		s = CHAR[tc-1]
		FIND = [0,0,0,0,0,0,0,0,0,0]
		#print (s)
		while len(s) != 0 :
			if 'Z' in s :
				s.remove('Z'); s.remove('E'); s.remove('R'); s.remove('O');
				FIND[0] += 1;
			elif 'W' in s :
				s.remove('T'); s.remove('W'); s.remove('O');
				FIND[2] += 1;
			elif 'U' in s :
				s.remove('F'); s.remove('O'); s.remove('U'); s.remove('R');
				FIND[4] += 1;
			elif 'X' in s :
				s.remove('S'); s.remove('I'); s.remove('X'); 
				FIND[6] += 1;
			elif 'G' in s :
				s.remove('E'); s.remove('I'); s.remove('G'); s.remove('H'); s.remove('T');
				FIND[8] += 1;
			elif 'H' in s :
				s.remove('T'); s.remove('H'); s.remove('R'); s.remove('E'); s.remove('E');
				FIND[3] += 1;
			elif 'F' in s :
				s.remove('F'); s.remove('I'); s.remove('V'); s.remove('E'); 
				FIND[5] += 1;
			elif 'O' in s :
				s.remove('O'); s.remove('N'); s.remove('E'); 
				FIND[1] += 1;
			elif 'S' in s :
				s.remove('S'); s.remove('E'); s.remove('V'); s.remove('E'); s.remove('N');
				FIND[7] += 1;
			elif 'N' in s :
				s.remove('N'); s.remove('I'); s.remove('N'); s.remove('E');					
				FIND[9] += 1;
		#print FIND
		for i in range(0, 10) :
			for k in range(0, FIND[i]) :
				result += "%d" % i

		result += "\n"
		f.write(result)

