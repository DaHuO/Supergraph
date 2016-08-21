infilename = 'B-large.in'
outfilename = 'outfile-large.txt'

def getResult(inputstring):
	inlist = list(map(lambda x: 0 if x == '-' else 1, inputstring.strip()))
	flip, prev = 0, None
	for pancake in inlist:
		if pancake != prev:
			flip += 1
		prev = pancake
	flip -= inlist[-1]
	return flip

if __name__ == '__main__':
	with open(infilename) as infile, open(outfilename, 'w') as outfile:
		case = 0
		for line in infile:
			if case > 0:
				outfile.write('Case #{0}: {1}\n'.format(case, getResult(line)))
			case += 1