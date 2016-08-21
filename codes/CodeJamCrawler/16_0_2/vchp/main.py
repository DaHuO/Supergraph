import sys

def changeMode(mode):
	if mode == '-':
		return '+'
	return '-'

def minFlip(stack):
	flip = 0
	n = len(stack)
	for i in range(1,n):
		if stack[i-1] != stack[i]:
			flip += 1
	if stack[-1] == '-':
		flip += 1
	return flip

inlist = []
infile = open(sys.argv[1],'r')
outfile = open('answer.out', 'w')
i = 1
skip = True
for line in infile:
	if skip:
		skip = False
		continue
	line = line.rstrip()
	output = 'Case #' + str(i) + ': ' + str(minFlip(line)) + '\n'
	outfile.write(output)
	i += 1
print('done')