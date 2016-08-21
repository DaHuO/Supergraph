def solve(string):
	previous = string[0]
	changes = 0
	for char in string[1:]:
		if(char != previous):
			previous = char
			changes += 1
	if(string[-1]=='-'):
		changes += 1
	return changes

if __name__=="__main__":
	ip = open("B-small.in")
	out = open("B-small.out", 'w')
	cases = int(ip.readline())
	for i in range(cases):
		pancakes = ip.readline().strip()
		x = solve(pancakes)
		out.write('Case #'+str(i+1)+': '+str(x)+'\n')
	ip.close()
	out.close()
