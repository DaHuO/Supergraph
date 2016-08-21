from sys import argv
def getWord(S):
	res = []
	largest = ord ('A')
	for c in S:
		if ord(c) >= largest:
			largest = ord(c)
			res.insert(0, c)
		else: 
			res.append(c)
	return res

script, filename = argv
lines = [line.rstrip('\n') for line in open(filename)]
lines.pop(0)

for i in range(0, len(lines)):
	print 'Case #' + str(i + 1) + ': ' + (''.join(getWord(lines[i])))
