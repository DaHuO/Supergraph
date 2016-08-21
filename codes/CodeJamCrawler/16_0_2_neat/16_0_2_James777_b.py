import sys
import optparse

debug = False

def reverseHere(here, i):
	there = [here[t] for t in range(len(here))]
	for k in range(i+1):
		if here[i-k] == '0':
			there[k]='1'
		else:
			there[k] = '0'
	return there

def solve(data):
	if debug:
		print '[+] inputdata %s' % str(data)

	ret = 0

	numData = int(''.join(data),2)
	queue = list()
	visited = [False for j in range(2**len(data))]

	if numData == 0:
		return 0
	queue.append([data,0])

	while len(queue) > 0:
		hereNode = queue.pop(0)
		here = hereNode[0]
		depth = hereNode[1]
		if debug:
			print '[+] queue pop %s' % str(here)
		numHere = int(''.join(here),2)
		visited[numHere] = True
		for i in range(len(here)):
				there = reverseHere(here, i)
				if debug:
					print '[+] adj[%d] %s' %(i,str(there))
				numThere = int(''.join(there),2)
				if numThere == 0:
					return depth + 1
				if visited[numThere] == False:
					queue.append([there, depth+1])


	return ret

def readData(infile):
	# R,C = map(int, infile.readline().strip().split())
	data = infile.readline().strip()
	data2 = []
	for i in range(len(data)):
		if data[i] == '+':
			data2.append('0')
		else:
			data2.append('1')

	return data2

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
