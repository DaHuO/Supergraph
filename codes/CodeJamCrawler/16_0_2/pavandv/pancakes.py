def getEnd(seq,start):
	start_sym = seq[start]
	idx = start+1;
	end = -1
	while idx < len(seq):
		if start_sym != seq[idx]:
			return idx
		idx+=1
	return -1

t = int(raw_input())
for i in range(0,t):
	seq = raw_input()
	operations = 0;
	if len(seq) == 0:
		print "Case #" + str(i+1) + ": "  + "0"
	else:
		start = 0
		end = getEnd(seq,start)
		last = seq[start]
		while end !=-1:
			operations+=1
			start = end
			end = getEnd(seq,start)
			last = seq[start]
		if last	== '-':
			operations+=1
		print "Case #" + str(i+1) + ": "  + str(operations)	