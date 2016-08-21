fin = open('A-large.in', 'r')
fout = open('A-large.out','w')


class Node:
	def __init__(self):
		self.nextNode = None
		self.prevNode = None
		self.val = "R"

def Recurse(N,tup):
	(R,P,S) = tup
	if N == 1:
		if (R,P,S) == (1,1,0):
			return "PR"
		elif (R,P,S) == (1,0,1):
			return "RS"
		elif (R,P,S) == (0,1,1):
			return "PS"
		else:
			return "IMPOSSIBLE"
	
	sortedlist = list(sorted([R,P,S]))
	
	if sortedlist[0] == sortedlist[1] and sortedlist[1] == sortedlist[2] - 1:
		first = (0,0,0)
		second = (0,0,0)
		m = max(sortedlist)/2
		
		if R == m*2:
			first = (m, m, m - 1)
			second = (m, m - 1, m)
		elif P == m*2:
			first = (m, m, m - 1)
			second = (m-1, m, m)
		else:
			first = (m - 1, m, m)
			second = (m, m - 1, m)
		
		firstout = Recurse(N-1, first)
		secondout = Recurse(N-1, second)
		
		if firstout == "IMPOSSIBLE" or secondout == "IMPOSSIBLE":
			return "IMPOSSIBLE"
		
		return firstout + secondout
	elif sortedlist[1] == sortedlist[2] and sortedlist[1] == sortedlist[0] + 1:
		first = (0,0,0)
		second = (0,0,0)
		m = min(sortedlist)/2
		
		if R == m*2:
			first = (m, m + 1, m)
			second = (m, m, m + 1)
		elif P == m*2:
			first = (m + 1, m, m)
			second = (m, m, m + 1)
		else:
			first = (m, m + 1, m)
			second = (m + 1, m, m)
		
		firstout = Recurse(N-1, first)
		secondout = Recurse(N-1, second)
		
		if firstout == "IMPOSSIBLE" or secondout == "IMPOSSIBLE":
			return "IMPOSSIBLE"
		
		return firstout + secondout
	else:
		return "IMPOSSIBLE"

numlines = int(fin.readline().rstrip())

for line in range(numlines):
	vals = str(fin.readline().rstrip())
	(N,R,P,S) = tuple([int(c) for c in vals.split(" ")])
	
	sortedlist = list(sorted([R,P,S]))
	result = Recurse(N,(R,P,S))
	
	outstr = "Case #" + str(line+1) + ": " + str(result) + "\n"
	# print result.rstrip()
	fout.write(outstr)


