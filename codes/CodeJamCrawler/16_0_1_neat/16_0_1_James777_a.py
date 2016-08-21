import sys
import optparse

debug = False

def setData(data, numList):
	ret = ''
	strData = str(data)
	
	for i in range(len(strData)):
		if debug:
			print '[+] numList ' + str(numList)
		cmp = strData[i]
		if cmp in numList:
			ret = cmp 
			numList.remove(cmp)
	return ret
			
def solve(data):
	if debug:
		print '[+] input data %d' % data
	if data == 0:
		return 'INSOMNIA'
	
	data2 = data
	numList = ['0','1','2','3','4','5','6','7','8','9']
	while len(numList) > 0 :	
		if debug:
			print '[+] checking data %d' % data2
		ret = setData(data2, numList)
		data2 += data
	return data2 - data

def readData(infile):
	# R,C = map(int, infile.readline().strip().split())
	return int(infile.readline().strip()) 

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
