#!/usr/bin/python
import sys
import binascii

#
def readFile(file):
	# lines(file)
	lines = [];
	for line in file:
		# print line
		lines.append(line)
	return lines;

def findMissing(list):
	dct = {}
	rst = []
	rstStr = ""
	for s in list:
		ary = s.split()
		for ns in ary:
			n = int(ns)
			if(n in dct):
				dct[n] = dct[n] + 1
			else:
				dct[n] = 1

	for key in dct:
		if(dct[key] % 2 == 1):
			rst.append(int(key))
	rst = sorted(rst)
	for i in range(0, len(rst)):
		rstStr += str(rst[i])
		if(i != len(rst) - 1):
			rstStr += ' '
	return rstStr



def main():
    file = open(sys.argv[1], "r+")
    rfile = open(sys.argv[2],'r+')
    print "file name: ", file.name
    lines = readFile(file)
    testNum = int(lines[0])
    print "testTotal:", testNum
    cnt = 1
    for i in range(0, testNum):
    	N = int(lines[cnt])
    	cnt += 1
    	# print "N:",N
    	list = []
    	for j in range(0, 2*N-1):
    		s = lines[cnt].strip()
    		list.append(s)
    		cnt += 1
    	r = findMissing(list)
    	r = "Case #"+str(i+1)+": " + str(r)
    	rfile.write(r+"\n")
    	



if __name__ == '__main__':
    main()