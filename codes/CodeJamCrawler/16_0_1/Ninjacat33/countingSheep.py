def someFunction(string):
	number = int(string)
	if number == 0:
		return "INSOMNIA"
	array = set(list(string))
	new = int(string)
	i = 2
	while array != set(list("0123456789")):
		new = number*i
		array.update(set(list(str(new))))
		i+=1
	return str(new)

f = open('A-large.in', 'r')
g = open('A-large.txt','w')

lines = int(f.readline())
for x in range(1,lines+1):
	last = someFunction(f.readline().strip('\n'))
	g.write("Case #%d: %s\r\n" %(x,last))

f.close()
g.close()