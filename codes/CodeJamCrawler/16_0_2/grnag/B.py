# 2016 qualifying round. problem B - pancakes

inFile =  open("B.large.in", "r")

T = int(inFile.readline().split()[0])

case = 1

def rev_str(s):
	return s[::-1]

while case <= T:
	stack =  inFile.readline().split()[0]
	
	rev_stack = rev_str(stack)
	
	ws = []
	for i in range(len(stack)):
		ws.append('+')
	
	#print "Case #{}: {} {} {} {}".format(case, stack, rev_stack, ws, ''.join(ws))
	index = 0
	count = 0
	while (rev_stack != ''.join(ws)):
		while(ws[index] == rev_stack[index]):
			index += 1
		count += 1
		for i in range(index, len(ws)):
			if ws[i] == '+':
				ws[i] = '-'
			else:
				ws[i] = '+'
		
	print "Case #{}: {}".format(case, count)
		
	
	case += 1
