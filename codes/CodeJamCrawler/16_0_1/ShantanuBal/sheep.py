f = open("input", "r")
o = open("output", "w")
n = int(f.readline())

def allZeroes(map):
	if map.count(0) == 10:
		return True
	return False

for x in range(n):
	m = int(f.readline())
	map = [1,1,1,1,1,1,1,1,1,1]
	getOut = False
	val = m
	if int(val) == 0:
		o.write("Case #" + str(x+1) + ": INSOMNIA" + "\n")
		continue
	while True:
		digits = str(val)
		print digits
		for each in digits:
			map[int(each)] = 0
			if allZeroes(map):
				o.write("Case #" + str(x+1) + ": " + digits + "\n")
				getOut = True
				break
		if getOut == True:
			break
		val += m


o.close()
f.close()
