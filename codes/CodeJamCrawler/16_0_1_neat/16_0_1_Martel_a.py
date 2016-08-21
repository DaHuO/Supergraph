from sys import argv

# Problem A. Counting Sheep

# N, number to try 
def countSheep (N, limit): 
	seen = {}
	seen['total'] = 0
	

	for i in range(1, limit):
		curStr = str(N * i)
		for c in curStr:
			if not c in seen:
				seen[c] = 1
				seen['total'] += 1
			
			if seen['total'] == 10:
				return curStr

	return 'INSOMNIA'


# T, number test cases
script, filename = argv
lines = [line.rstrip('\n') for line in open(filename)]
lines.pop(0)

for i in range(0, len(lines)):
	print 'Case #' + str(i + 1) + ': ' + str(countSheep(int(lines[i]), 1000000))
