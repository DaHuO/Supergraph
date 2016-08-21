from sys import argv
# Problem B

def countSheep (a): 
	count = 0
	for i in range(len(a) -1, -1, -1):
	 	if a[i] == 0:
	 		count += 1
	 		for j in range(0, i):
	 			a[j] = (a[j] + 1) % 2
	 		
	return count


# T, number test cases
script, filename = argv
lines = [line.rstrip('\n') for line in open(filename)]
lines.pop(0)

for i in range(0, len(lines)):
	cur = lines[i]
	res = []
	for j in range(0, len(cur)):
		if  cur[j] == '+':
			res.append(1)
		else: 
			res.append(0)

	print 'Case #' + str(i + 1) + ': ' + str(countSheep(res))
