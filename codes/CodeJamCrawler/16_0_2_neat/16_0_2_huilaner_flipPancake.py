#!/usr/bin/python
import sys
import binascii


def readFile(file):
	# lines(file)
	lines = [];
	for line in file:
		# print line
		lines.append(line)
	return lines;

def flip(s):
	s = s.rstrip()
	prevUP = False
	cnt = 0
	i = 0
	n = len(s)
	while(i < n):
		if(s[i] == '+'):
			while(i < n and s[i] == '+'):
				prevUP = True
				i += 1
		else:
			cnt += 1
			if(prevUP == True):
				cnt += 1
			prevUP = False
			while(i < n and s[i] == '-'):
				i += 1
	return cnt



def main():
    file = open(sys.argv[1], "r+")
    rfile = open(sys.argv[2],'r+')
    print "file name: ", file.name
    lines = readFile(file)
    testNum = int(lines[0])
    print "testTotal:", testNum
    for i in range(1, testNum+1):
    	r = flip(lines[i])
    	r = "Case #"+str(i)+": "+str(r)
    	# print r
    	rfile.write(r+"\n")



if __name__ == '__main__':
    main()