import sys	

def add_digits(number, found_set):
	while number > 0:
		digit = number % 10
		found_set.add(digit)
		number /= 10

def find_number(N):
	i = 1
	found_set = set()
	while len(found_set) < 10:
		number = i*N
		add_digits(number,found_set)
		i += 1
	return number

def solveCase(case, f, fout):
	N = int(f.readline().strip())
	if N == 0:
		result = 'INSOMNIA'
	else:
		result = find_number(N)
	writeLine(fout, case, str(result))

def writeLine(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	inputFileName = sys.argv[1]
	
	f = file(inputFileName)
	fout = file("%s.out" %(inputFileName.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solveCase(case + 1, f, fout)
		
	f.close()
	fout.close()
