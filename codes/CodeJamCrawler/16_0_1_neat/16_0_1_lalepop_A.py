def algo(line):
	a = set(line.strip())
	val = int(line.strip())
	if val == 0:
		return 'INSOMNIA'
	N = 2
	while(len(a) < 10):
		b = set(str(val*N))
		a = a.union(b)
		N+=1
		
	return str(val*(N-1))

if __name__ == '__main__':
	
	fout = open('A-large.out', 'w')

	with open('A-large.in','r') as fin:
		number_of_cases = fin.readline()
	
		case = 1
		for line in fin.readlines():
			#print(line)
			ans = algo(line)
			fout.write("Case #{0}: {1}\n".format(str(case), ans))
			case += 1

	fout.close()
