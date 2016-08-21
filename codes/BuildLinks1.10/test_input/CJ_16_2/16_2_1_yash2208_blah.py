outfile = open("output.txt", 'w')
with open("A-large.in",'r') as inputfile:
	for _ in xrange(int(inputfile.readline())):
		a,ans=list(inputfile.readline()),""
		while 'Z' in a:
			a.remove('Z')
			a.remove('E')
			a.remove('R')
			a.remove('O')
			ans+="0"
		while 'X' in a:
			a.remove('S')
			a.remove('I')
			a.remove('X')
			ans+="6"
		while 'W' in a:
			a.remove('T')
			a.remove('W')
			a.remove('O')
			ans+="2"
		while 'U' in a:
			a.remove('F')
			a.remove('U')
			a.remove('O')
			a.remove('R')
			ans+="4"
		while 'V' in a and 'F' in a:
			a.remove('F')
			a.remove('I')
			a.remove('V')
			a.remove('E')
			ans+="5"
		while 'G' in a and 'I' in a:
			a.remove('E')
			a.remove('I')
			a.remove('G')
			a.remove('H')
			a.remove('T')
			ans+="8"
		while 'I' in a and 'N' in a:
			a.remove('N')
			a.remove('I')
			a.remove('N')
			a.remove('E')
			ans+="9"
		while 'R' in a:
			a.remove('E')
			a.remove('R')
			a.remove('E')
			a.remove('H')
			a.remove('T')
			ans+="3"
		while 'V' in a:
			a.remove('E')
			a.remove('S')
			a.remove('V')
			a.remove('E')
			a.remove('N')
			ans+="7"
		ans += ("1"*(len(a)/3))
		outfile.write("Case #" + str(_+1) + ": " + "".join(sorted(ans)) + "\n")