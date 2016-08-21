#!/usr/bin/env python

def readSheepIn(filename):
 	mylist = [int(line.rstrip()) for line in open(filename)]
 	mylist.pop(0)
 	return mylist

def writeSheepOut(output, filename):
	file = open(filename, "w")
	for i in range(0,len(output)):
		file.write("Case #%d: %s\n" % (i+1, output[i]))
	file.close()

def countingSheep(n):
	if n == 0:
		return "INSOMNIA"
	digits=[False]*10 # (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9)
	m=0
	while reduce(lambda x, y: x & y, digits) == False:
		m = n+m
		m_str=str(m)
		for d in m_str:
			digits[int(d)] = True
	print m
	return str(m)

def main():
	l = readSheepIn("A-large.in")
	output = []
	for n in l:
		print "... current n =", n
		output.append(countingSheep(n))
	print output
	writeSheepOut(output, "sheep_large.out")

if __name__ == "__main__":
    main()