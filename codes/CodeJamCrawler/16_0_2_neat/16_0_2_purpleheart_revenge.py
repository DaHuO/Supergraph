import sys

def is_flipped(arr):
	return arr.count("+") == len(arr)

def minimise(arr):
	toret = []
	last = ""
	for aval in arr:
		if aval != last:
			toret.append(aval)
		last = aval
	return toret
f = open(sys.argv[1],"r")
n = int(f.readline())
c = 1
while n > 0:
	x = minimise(list(f.readline().strip()))
	lenx = len(x)
	answer = 0
	n -= 1
	if lenx == 1:
		if x[0] == "-":
			answer += 1
	else:
		ind = 1
		last = x[0]
		if last == "-":
			answer += 1
		while ind < lenx:
			this = x[ind]
			if this == "-":
				if last == "+":
					answer	+= 2
				else:
					answer += 1
			last = this
			ind += 1
	print ("Case #%d: %s")%(c, answer)
	c += 1	
