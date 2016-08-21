def flipPancakes(part):
	if len(part) != 1:
		part.reverse()
	d = {"+":"-","-":"+"}
	portion = [d.get(face) for face in part]
	return portion

def someFunction(string):
	stack = list(string)
	count = 0
	while stack.count('-') != 0:
		if len(stack) == 1:
			stack[0] = '+'
			count+=1
		elif stack[0] == '+':
			i = 1
			while stack[i] == '+':
				i+=1
			stack[0:i] = flipPancakes(stack[0:i])[0]
			count+=1
		elif stack[0] == '-':
			i = 1
			while (i < len(stack)) and (stack[i] == '-'):
				i+=1
			stack[0:i] = flipPancakes(stack[0:i])[0]
			count+=1
	return count

f = open('B-large.in', 'r')
g = open('B-large.txt','w')

lines = int(f.readline())
for x in range(1,lines+1):
	flip = someFunction(f.readline().strip("\r\n"))
	g.write("Case #%d: %d\r\n" %(x,flip))

f.close()
g.close()