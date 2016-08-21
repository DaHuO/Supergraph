def build_slides(B, M):
	if M > 2**(B-2):
		return 'IMPOSSIBLE'
	result = 'POSSIBLE\n'
	b = M - 1
	first_line = bin(b).split('b')[1] + '1'
	result += (B - len(first_line))*'0' + first_line + '\n'
	for i in xrange(2, B + 1):
		result += i*'0' + (B - i)*'1'+'\n'
	return result.strip()

def solveCase(case, f, fout):
	B, M = f.readline().strip().split(' ')
	B = int(B)
	M = int(M)
	result = build_slides(B,M)
	writeLine(fout, case, result)

def writeLine(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	inputFileName = 'B-large.in'
	
	f = file(inputFileName)
	fout = file("%s.out" %(inputFileName.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solveCase(case + 1, f, fout)
		
	f.close()
	fout.close()
