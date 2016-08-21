import sys
import optparse

debug = False


def next(data, length):
	ret = False
	for i in range(1,length-1):
		if data[length - i -1] == '0':
			data[length -i -1] = '1'
			ret = True
			break
		else:
			data[length -i -1] = '0'

	return ret




def solve(data):
	rets = []
	ret = []
	strRet = '\n'
	if debug:
		print '[+] inputdata %d, %d' %(data[0],data[1])

	binNum = ['0' for x in range(data[0])]
	binNum[0] = '1'
	binNum[-1] = '1'
	keep = True
	while keep:
		if debug:
			print '[+] binNum %s' % str(binNum)

		ret = []
		strNum = ''.join(binNum)
		ret.append(strNum)
		found = False
		for base in range(2,11):
			baseNum = int(strNum, base)
			found = False
			if debug:
				print '[+] baseNum %d' % baseNum
			#for div in range(2, baseNum):
			for div in range(2, 10000):
				if baseNum % div == 0:
					ret.append(str(div))
					found = True
					break
			if len(ret) == 10:
				break		
			if found == False:
				break
		if found == True:
			rets.append(ret)

		if len(rets) == data[1]:
			break
		keep = next(binNum, len(binNum))

	for i in range(len(rets)):
		strRet += ' '.join(rets[i])
		if i< len(rets) - 1:
			strRet += '\n'

	return strRet

def readData(infile):
	N,J = map(int, infile.readline().strip().split())
	return N,J

def howto():
	usage = ' -i <input file> [-o <output file>]'
	parser = optparse.OptionParser(sys.argv[0] + usage)
	parser.add_option(
		'-i', dest='infile', type='string', help='specify infile name')
	parser.add_option(
		'-o', dest='outfile', type='string', help='specify outfile name')
	(options, args) = parser.parse_args()
	if options.infile is None:
		print parser.usage
	return options.infile, options.outfile

if __name__ == '__main__':
	infile, outfile = howto()
	if infile is None:
		exit()

	infile = open(infile, 'r')
	if outfile is not None:
		outfile = open(outfile, 'w')

	T = int(infile.readline().strip())
	for caseN in xrange(1, T + 1):
		data = readData(infile)
		result = solve(data)
		resultForm = 'Case #%i: %s\n' % (caseN, result)

		if outfile:
			outfile.write(resultForm)
		else:
			print resultForm

	infile.close()
	if outfile is not None:
		outfile.close()
