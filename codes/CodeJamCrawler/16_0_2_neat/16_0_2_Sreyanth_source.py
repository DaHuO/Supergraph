# your code goes here

def all_pos(string):
	if string.count("+") == len(string):
		return True
	a = ""
	b = string[0]
	rofl = False
	for i in string:
		if i != b:
			rofl = True
		if not rofl:
			if i == "+":
				a += "-"
			else:
				a += "+"
		else:
			a += i
	return a		

t = int(raw_input())

for i in range(t):
	cur = raw_input()
	f = 0
	n = cur
	while True:
		n = all_pos(n)
		if n == True:
			print "Case #%d: %d" % (i+1, f)
			break
		else:
			f+= 1