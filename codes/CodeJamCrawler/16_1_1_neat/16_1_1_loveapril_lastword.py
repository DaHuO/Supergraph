def lastword(word):
	letters = [ord(i) for i in list(word)]

	l = len(letters)
	sol = []
	a = None
	b = None
	for  i in range(l):
		if len(sol) ==0:
			sol.append(letters[i])
			a = sol[0]
		else:
			if letters[i] >= a:
				sol.insert(0,letters[i])
				a = sol[0]
			else:
				sol.append(letters[i])

	return ''.join(chr(i) for i in sol)



def main():
	filename = 'A-large.in'
	output = 'A-large.out'
	f = open(filename,'r')
	#Output file
	out = open(output,'w')
	while True:
		line = f.readline()
		if line == '':
			break
		num_tests = int(line)
		for i in xrange(num_tests):
			line = f.readline().strip()
			sol = lastword(line)
			s = 'Case #%s: ' %(i+1)
			s = s + str(sol)
			out.write(s)
			out.write('\n')
		
if __name__ == "__main__":
	main()